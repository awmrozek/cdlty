import asyncio
from bleak import BleakClient, BleakScanner

# LEGO Wireless Protocol (LWP3) UUIDs
LWP3_HUB_UUID = "00001623-1212-efde-1623-785feabcd123"  # LEGO Hub Service UUID
CHARACTERISTIC_UUID = "00001624-1212-efde-1623-785feabcd123"  # LEGO Hub Write Characteristic

# Motor ports
PORT_A = 0x00  # Port A
PORT_B = 0x01  # Port B

MSG_TYPES = {
    0x01: "Hub Properties",
    0x02: "Hub Actions",
    0x03: "Hub Alerts",
    0x04: "Hub Attached I/O",
    0x05: "Generic Error",
    0x43: "Port information"
    # Add others as needed, e.g., 0x21 Port Info, etc.
}

ERROR_CODES = {
    0x01: "ACK",
    0x02: "MACK",
    0x03: "Buffer Overflow",
    0x04: "Timeout",
    0x05: "Command NOT recognized",
    0x06: "Invalid use",
    0x07: "Overcurrent",
    0x08: "Internal ERROR",
}



async def connect_and_drive():
    print("Scanning for Lego Technic Hub...")
    devices = await BleakScanner.discover()

    # Find the Technic Hub
    hub = None
    for d in devices:
        if "Technic" in d.name or "Hub" in d.name:
            hub = d
            break

    if not hub:
        print("No Lego Technic Hub found.")
        return

    print(f"Connecting to {hub.name} [{hub.address}]...")

    async with BleakClient(hub.address) as client:
        print("Connected.")

        def create_port_info_request(port: int, info_type: int):
            return bytearray([
                0x05,       # Length
                0x00,       # Hub ID
                0x21,       # Port Information Request
                port,       # Port ID (0x00 = A)
                info_type   # Info Type (e.g., 0x01 = Mode Info)
            ])

        def notification_handler(sender, data):
            print(f"Notify: {decode_lwp_message(data)}")

        # Function to send a direct motor command
        def drive_motor(port, power):
            # Format:
            # Port output command: 0x81
            # Port
            # Start power (0x11 = set power)
            # Power level (-100 to 100)
            # Execution flag: 0x00 = don't buffer, execute immediately
            # return bytearray([0x81, port, 0x11, power & 0xFF, 0x00])
            return bytearray([0x0a, 0x00, 0x81, port, 0x00, 0x51, 0x01, 0x64, 0x00])

        def parse_header(data):
            length = data[0] & 0x7F
            hub_id = data[1]
            msg_type = data[2]
            return length, hub_id, msg_type

        def decode_error(data):
            cmd, code = data[3], data[4]
            desc = ERROR_CODES.get(code, f"Unknown error code 0x{code:02X}")
            return f"Error from cmd 0x{cmd:02X}: {desc}"

        def decode_hub_properties(data):
            # For demo: show payload hex
            return f"Hub Properties Data: {data[3:].hex()}"

        def decode_hub_alerts(data):
            return f"Alert (type 0x{data[3]:02X}): payload {data[4:].hex()}"

        def decode_attached_io(data):
            port = data[3]
            dev_id = data[4]
            return f"I/O attached: Port 0x{port:02X}, Device 0x{dev_id:02X}"

        def decode_port_information(data):
            return f"PORT_INFORMATION"

        def decode_lwp_message(data):
            if len(data) < 3:
                return "Too short to parse"
            length, hub_id, msg_type = parse_header(data)
            typ_name = MSG_TYPES.get(msg_type, f"Unknown Message Type 0x{msg_type:02X}")
            payload = data[:length]
            body = {
                0x01: decode_hub_properties,
                0x03: decode_hub_alerts,
                0x04: decode_attached_io,
                0x05: decode_error,
                0x43: decode_port_information
            }.get(msg_type, lambda d: f"Handler not implemented for {typ_name}")
            return f"{typ_name} (hub {hub_id}): " + body(payload)

        print("Driving forward for 3 seconds...")
        await client.start_notify(CHARACTERISTIC_UUID, notification_handler)
        await asyncio.sleep(2)
        for port in [0x01, 0x03, 0x32, 0x3B, 0x3C, 0x3D, 0x60, 0x61, 0x62, 0x63, 0x64]:
            await client.write_gatt_char(CHARACTERISTIC_UUID, create_port_info_request(port, 1), response=True)
            await client.write_gatt_char(CHARACTERISTIC_UUID, drive_motor(port, 50), response=True)
        await asyncio.sleep(3)

        print("Done.")

asyncio.run(connect_and_drive())
