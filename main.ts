control.onEvent(EventBusSource.MES_DPAD_CONTROLLER_ID, EventBusValue.MICROBIT_EVT_ANY, function () {
    if (lastValue != control.eventValue()) {
        lastValue = control.eventValue()
        led.stopAnimation()
        if (control.eventValue() == 1) {
            iBIT.setMotor(ibitMotorCH.M1, ibitMotor.Forward, 30)
            iBIT.setMotor(ibitMotorCH.M2, ibitMotor.Forward, 25)
        } else if (control.eventValue() == 2) {
            iBIT.setMotor(ibitMotorCH.M1, ibitMotor.Forward, 0)
            iBIT.setMotor(ibitMotorCH.M2, ibitMotor.Forward, 0)
        } else if (control.eventValue() == 3) {
            iBIT.setMotor(ibitMotorCH.M1, ibitMotor.Backward, 30)
            iBIT.setMotor(ibitMotorCH.M2, ibitMotor.Backward, 25)
        } else if (control.eventValue() == 4) {
            iBIT.setMotor(ibitMotorCH.M1, ibitMotor.Backward, 0)
            iBIT.setMotor(ibitMotorCH.M2, ibitMotor.Backward, 0)
        } else if (control.eventValue() == 5) {
            iBIT.setMotor(ibitMotorCH.M1, ibitMotor.Forward, 30)
        } else if (control.eventValue() == 6) {
            iBIT.setMotor(ibitMotorCH.M1, ibitMotor.Forward, 0)
        } else if (control.eventValue() == 7) {
            iBIT.setMotor(ibitMotorCH.M2, ibitMotor.Forward, 25)
        } else if (control.eventValue() == 8) {
            iBIT.setMotor(ibitMotorCH.M2, ibitMotor.Forward, 0)
        } else if (control.eventValue() == 9) {
            basic.showString("1")
        } else if (control.eventValue() == 10) {
            basic.showString("1 Up")
        } else if (control.eventValue() == 11) {
            basic.showString("2")
        } else if (control.eventValue() == 12) {
            basic.showString("2 Up")
        } else if (control.eventValue() == 13) {
            basic.showString("3")
        } else if (control.eventValue() == 14) {
            basic.showString("3 Up ")
        } else if (control.eventValue() == 15) {
            basic.showString("4")
        } else if (control.eventValue() == 16) {
            basic.showString("4 Up")
        } else {
            basic.clearScreen()
        }
    }
})
let lastValue = 0
lastValue = 0
bluetooth.startLEDService()
basic.showIcon(IconNames.Heart)
