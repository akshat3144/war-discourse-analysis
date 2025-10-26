import asyncio
import os
import json
from datetime import datetime, timezone
from typing import List, Dict

import pandas as pd
from dotenv import load_dotenv
from telethon import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest

load_dotenv()  # Load environment variables from .env file

# Telegram API credentials from environment
API_ID = os.getenv("TELEGRAM_API_ID")
API_HASH = os.getenv("TELEGRAM_API_HASH")
PHONE = os.getenv("TELEGRAM_PHONE")


class TelegramCollector:
    def __init__(self, api_id: str, api_hash: str, phone: str):
        self.api_id = api_id
        self.api_hash = api_hash
        self.phone = phone
        self.client = TelegramClient("session_name", api_id, api_hash)
        self.data = []

    async def connect(self):
        """Connect to Telegram."""
        await self.client.start(phone=self.phone)
        print("✓ Connected to Telegram")

    async def collect_channel_messages(
        self,
        channel_username: str,
        start_date: datetime = None,
        end_date: datetime = None,
        limit: int = None,
    ) -> List[Dict]:
        """Collect messages from a single channel."""
        messages = []
        try:
            entity = await self.client.get_entity(channel_username)
            print(f"\nCollecting messages from @{entity.username}...")
            
            async for message in self.client.iter_messages(
                entity, limit=limit, offset_date=start_date
            ):
                if start_date and message.date < start_date:
                    continue
                if end_date and message.date > end_date:
                    continue

                msg_data = {
                    "message_id": message.id,
                    "channel_name": entity.username,
                    "message_text": message.text or "",
                    "timestamp": message.date.isoformat() if message.date else None,
                    "views": message.views or 0,
                    "forwards": message.forwards or 0,
                    "media_type": type(message.media).__name__ if message.media else "text",
                    "has_media": message.media is not None,
                    "reply_to": message.reply_to_msg_id,
                    "collected_date": datetime.now().isoformat(),
                }
                messages.append(msg_data)

                if len(messages) % 100 == 0:
                    print(f"Collected {len(messages)} messages so far...")
            
            self.data.extend(messages)
            print(f"Total messages collected from @{entity.username}: {len(messages)}")
            return messages

        except Exception as e:
            print(f"✗ Error collecting from @{channel_username}: {str(e)}")
            return []

    async def collect_from_multiple_channels(
        self,
        channels: List[str],
        start_date: datetime,
        end_date: datetime,
        limit_per_channel: int = None,
    ) -> Dict[str, List[Dict]]:
        """Collect messages from multiple channels."""
        all_data = {}
        for channel in channels:
            messages = await self.collect_channel_messages(
                channel, start_date, end_date, limit_per_channel
            )
            all_data[channel] = messages
            await asyncio.sleep(1)  # Rate limiting
        return all_data

    def save_data(self, data: Dict[str, List[Dict]], output_file: str):
        """Save collected data to JSON and create a summary."""
        all_messages = []
        for channel, messages in data.items():
            all_messages.extend(messages)

        os.makedirs(os.path.dirname(output_file), exist_ok=True)

        # Save full data
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(all_messages, f, ensure_ascii=False, indent=2)
        print(f"✓ Saved {len(all_messages)} messages to {output_file}")

        # Save summary
        summary = {
            "total_messages": len(all_messages),
            "channels": {channel: len(messages) for channel, messages in data.items()},
            "collection_date": datetime.now().isoformat(),
        }
        summary_file = output_file.replace(".json", "_summary.json")
        with open(summary_file, "w", encoding="utf-8") as f:
            json.dump(summary, f, ensure_ascii=False, indent=2)
        print(f"✓ Saved summary to {summary_file}")

    async def disconnect(self):
        """Disconnect from Telegram."""
        await self.client.disconnect()
        print("✓ Disconnected from Telegram")


async def main():
    # Channels to collect from
    CHANNELS = [
        "AlQassamBrigades",
        "Aqsatvsat",
        "Eyeonpalestine",
        "FreePalestine2023",
        "GazaNow",
        "PalestineSolidarityBelgium",
        "PalestineUpdates",
        "PalestinianResistance",
        "StopGazaGenocide",
        "TIMESOFGAZA",
        "TheJerusalemPost",
        "bigolivr",
        "gazaalanpa",
        "gazaenglishupdates",
        "haqqintel",
        "palOnline",
        "palestineonline",
        "palestineresistance",
        "resistancechain"
    ]

    # Date range
    START_DATE = datetime(2023, 10, 23, tzinfo=timezone.utc)
    END_DATE = datetime(2025, 1, 20, tzinfo=timezone.utc)

    # Initialize collector
    collector = TelegramCollector(API_ID, API_HASH, PHONE)

    try:
        await collector.connect()
        data = await collector.collect_from_multiple_channels(
            CHANNELS, START_DATE, END_DATE, limit_per_channel=None
        )
        output_file = f"collected_data/telegram_data_{datetime.now().strftime('%Y%m%d')}.json"
        collector.save_data(data, output_file)
    finally:
        await collector.disconnect()


if __name__ == "__main__":
    asyncio.run(main())
