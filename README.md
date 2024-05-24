# GREE WiFi Modules Firmware

Here are known firmwares for GREE Air Conditioners WiFi Modules. 
Each folder means **firmwareCode** of the device.
Inside each folder you'll find firmwares.

## Known modules architechtures

### Armv8
- 36300000257
- 362001063066 (RK3308)

### Armv7E-M
- 362001060200
- 362001060297
- 362001060498 (MTK7682)
- 362001060499
- 362001065279 (RTL8720CF)
- 362001065280 (RTL8710C)

### Xtensa
- 36200100812
- 362001061890 (ESP32)

### RISC-V 32bit
- 362001065232 (ESP32C3)

### Unknown
- 362001000835
- 362001062107

## Fetch metadata for your `firmwareCode`

Create python virtual environment, install `requests` module with `pip`:

```sh
~/ python3 -m vev .venv
~/ source .venv/bin/activvate
~/ pip install requests
```

Now you'll be able to run the script:

```sh
~/ python firmwareFetch.py
Usage: python script.py <firmware_code>
```

The script will create `downloaded` folder and place `.md` docs under it for each `*grih.gree.com` server.
Here is an example:

```sh
~/ python firmwareFetch.py 362001065279
Ignore firmware code 362001065279 from grih.gree.com due to response status 405
Data saved for firmware code 362001065279 from tmp.grih.gree.com
Data saved for firmware code 362001065279 from kfgrih.gree.com
Data saved for firmware code 362001065279 from test.grih.gree.com
Error fetching data for firmware code 362001065279 from ru.grih.gree.com: 404 Client Error: Not Found for url: http://ru.grih.gree.com/wifiModule/Lastversion?firmwareCode=362001065279
Ignore firmware code 362001065279 from na.grih.gree.com due to response status 405
Ignore firmware code 362001065279 from hk.grih.gree.com due to response status 405
Ignore firmware code 362001065279 from eu.grih.gree.com due to response status 405
Ignore firmware code 362001065279 from in.grih.gree.com due to response status 405
Ignore firmware code 362001065279 from sa.grih.gree.com due to response status 405
~/ ls ./downloaded
362001065279_v1.22_kfgrih.gree.com.md    362001065279_v1.22_test.grih.gree.com.md 362001065279_v1.22_tmp.grih.gree.com.md
```

When you're done, deactivate your python virtual environment.

```sh
~/ deactivate
```

## How theese firmwares were got
From an old version of Android mobile application hardcoded
**firmwareCode** were extracted.

Using theese codes you can continue to
`http://{GREE_SERVER}/wifiModule/Lastversion?firmwareCode=`
and get a firmware download link.

There can be different updates for different regions.
Known servers:
```
grih.gree.com
tmp.grih.gree.com
test.grih.gree.com
kfgrih.gree.com
ru.grih.gree.com
na.grih.gree.com
hk.grih.gree.com
eu.grih.gree.com
in.grih.gree.com
sa.grih.gree.com
```

### Example
```sh
~/ curl 'https://grih.gree.com/wifiModule/Lastversion?firmwareCode=36300000257' 2>/dev/null | jq
```
```json
{
  "CreateDate": "2023-06-05 03:12:16",
  "commProtVer": "V1.0.0",
  "desc": "",
  "forcedUpgrade": 1,
  "frcUpgdType": 0,
  "r": 200,
  "url": "http://grih.gree.com/wifiModule/image/10527/274288",
  "ver": "3.4"
}
```
