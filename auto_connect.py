 
# SPDX-License-Identifier: MIT
# Copyright (c) 2020 Henrik Blidh
# Copyright (c) 2022-2023 The Pybricks Authors

"""
Automatischer Start des Hub-Programms per Bluetooth
"""

import asyncio
from contextlib import suppress
from bleak import BleakScanner, BleakClient

PYBRICKS_COMMAND_EVENT_CHAR_UUID = "c5f50002-8280-46da-89f4-6d8051e4aeef"
HUB_NAME = "Pybricks Hub"  # Anpassen falls notwendig

async def main():
    main_task = asyncio.current_task()

    def handle_disconnect(_):
        print("Verbindung getrennt.")
        if not main_task.done():
            main_task.cancel()

    ready_event = asyncio.Event()

    def handle_rx(_, data: bytearray):
        if data[0] == 0x01:
            payload = data[1:]
            if payload == b"rdy":
                ready_event.set()
            else:
                print("Empfangen:", payload)

    # Verbindung herstellen
    device = await BleakScanner.find_device_by_name(HUB_NAME)
    if device is None:
        print(f"Hub '{HUB_NAME}' nicht gefunden")
        return

    async with BleakClient(device, handle_disconnect) as client:
        await client.start_notify(PYBRICKS_COMMAND_EVENT_CHAR_UUID, handle_rx)

        async def send(data):
            await ready_event.wait()
            ready_event.clear()
            await client.write_gatt_char(
                PYBRICKS_COMMAND_EVENT_CHAR_UUID,
                b"\x06" + data,
                response=True
            )

        # 🔥 Wichtigster Teil: Startbefehl senden 🔥
        print("Starte Programm auf dem Hub...")
        await client.write_gatt_char(
            PYBRICKS_COMMAND_EVENT_CHAR_UUID,
            # Befehl 0x01 = Starte Nutzerprogramm
            b"\x01",  # Magic Byte zum Programmstart
            response=True
        )

        # Warte bis der Hub bereit ist
        await ready_event.wait()

        # Steuerbefehle senden
        print("Sende Steuerbefehle...")
        await send(b"fwd")
        await asyncio.sleep(2)
        await send(b"bkw")
        await asyncio.sleep(2)
        await send(b"bye")

        print("Fertig!")

if __name__ == "__main__":
    with suppress(asyncio.CancelledError):
        asyncio.run(main())
