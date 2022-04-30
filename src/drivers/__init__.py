import logging

logger = logging.getLogger('drivers')


class ChassisDriver:
    async def move(self, direction: float, speed: float, distance: float = None):
        logger.debug('move %s %s %s', direction, speed, distance)
        pass

    async def rotate(self, speed: float):
        logger.debug('rotate %s', speed)
        pass


class ArmDriver:
    async def arm_up(self, speed):
        logger.debug('arm up %s', speed)
        pass

    async def arm_spray(self, time):
        logger.debug('arm spray %s', time)
        pass

    def capture_image(self):
        logger.debug('capture image %s')
        pass
