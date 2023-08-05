import asyncio
import logging
from typing import List

import aiolifx


logger = logging.getLogger(__name__)


class Bulbs:
    def __init__(self, loop: asyncio.AbstractEventLoop):
        self._loop = loop
        self.bulbs = []  # type: List[aiolifx.aiolifx.Light]

    def register(self, bulb: aiolifx.aiolifx.Light) -> None:
        logger.debug("register light %s", bulb.mac_addr)
        self._loop.create_task(self.async_register(bulb))

    async def async_register(self, bulb: aiolifx.aiolifx.Light) -> None:
        await bulb.get_metadata(loop=self._loop)
        self.bulbs.append(bulb)
        logger.info("got light %s (%s)", bulb.mac_addr, bulb.label)

    def unregister(self, bulb: aiolifx.aiolifx.Light) -> None:
        logger.info("unregister light %s (%s)", bulb.mac_addr, bulb.label)
        idx = 0
        for x in list([y.mac_addr for y in self.bulbs]):
            if x == bulb.mac_addr:
                del(self.bulbs[idx])
                break
            idx += 1

    def get_group(self, group: str) -> 'Bulbs':
        result = Bulbs(self._loop)
        result.bulbs = list(filter(lambda b: b.group == group, self.bulbs))
        return result

    def get_label(self, label: str) -> 'Bulbs':
        result = Bulbs(self._loop)
        result.bulbs = list(filter(lambda b: b.label == label, self.bulbs))
        return result

    async def wake_up(self) -> None:
        for bulb in self.bulbs:
            power = await bulb.get_power()
            if not power:
                await bulb.set_color([58275, 0, 0, 2500])
            await bulb.set_power(True)
            await bulb.set_color([58275, 0, 65365, 2500], duration=60000)

    async def flash(self) -> None:
        for bulb in self.bulbs:
            # transient, color, period,cycles,duty_cycle,waveform
            await bulb.set_waveform({
                "color": [0, 0, 0, 3500],
                "transient": 1,
                "period": 100,
                "cycles": 30,
                "duty_cycle": 0,
                "waveform": 0
            })

    def __str__(self):
        return ", ".join([str(b.label) for b in self.bulbs])
