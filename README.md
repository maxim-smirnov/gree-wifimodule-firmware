# GREE WiFi Modules Firmware

Here are known firmwares for GREE Air Conditioners WiFi Modules. 
Each folder means **firmwareCode** of the device.
Inside each folder you'll find firmwares.

## Known modules architechtures

### ARMv8
- 36300000257

### Xtensa
- 36200100812

### Unknown
- 362001060297

## How theese firmwares were got
From an old version of Android mobile application hardcoded
**firmwareCode** were extracted.

Using theese codes you can continue to
`https://{GREE_SERVER}/wifiModule/Lastversion?firmwareCode=`
and get a firmware download link.

There can be different updates for different regions.
Known servers:
```
grih.gree.com
test.grih.gree.com
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
