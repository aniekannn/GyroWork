from autoroutine import AutoRoutine
from wpimath.controller import PIDController


class DriveStraight(AutoRoutine):

    def __init__(self, drivetrain, goal_in_meters):
        self.drivetrain = drivetrain
        self.goal = goal_in_meters
        self.pid_controller = PIDController(20, 0, 0 )
        self.pid_controller.setSetpoint(0)
        self.pid_controller.setTolerance(.05)
        self.pid_controller.setDistance(25)


    def run(self):
        difference = self.drivetrain.getLeftDistanceMeter()-self.drivetrain.getRightDistanceMeter()
        rotate = self.pid_controller.calculate(difference)
        distance_difference = self.drivetrain.goalDistance() - self.drivetrain.goalDistance
        forward = self.pid_controller.calculate(difference)

        if self.pid_controller.atSetpoint():
            rotate = 0
            forward = 0
        if self.drivetrain.averageDistanceMeter() > self.goal:
            self.drivetrain.arcadeDrive(0, 0)

        else:
            rotate = difference
            # rotate=0
            forward = 4
            print(f"Fwd: {forward}, Rot: {rotate}, distance:{self.drivetrain}, difference{difference}")
            self.drivetrain.arcadeDrive(rotate, forward)
