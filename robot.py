import os
import wpilib
from wpilib import TimedRobot
from robotcontainer import RobotContainer


class MyRobot(TimedRobot):  # this is the controller
    def robotInit(self) -> None:
        self.container = RobotContainer()

    def robotPeriodic(self) -> None:
        ...

    def teleopPeriodic(self) -> None:
        forward = self.container.controller.getRawAxis(0)
        rotate = self.container.controller.getRawAxis(1)
        self.container.drivetrain.arcadeDrive(rotate, forward)
        print(f"Forward: {forward}, Rotate: {rotate}")

    def autonomousInit(self) -> None:
        self.auto = self.container.get_autonoumous()

    def autonoumousPeriodic (self) -> None:
        self.autonomous_controller.run()
        # pull controller
        # invoke drivetrain, move

    def autonomousExit(self) -> None:
        self.drivetrain.resetEncoders()
        self.container.drivetrain.resetGyro()

    def disabledInit(self) -> None:
        ...

if __name__ == "__main__":
    os.environ["HALSIMWS_HOST"] = "10.0.0.2"
    os.environ["HALSIMWS_PORT"] = "3300"

    wpilib.run(MyRobot)