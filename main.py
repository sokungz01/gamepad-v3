def on_mes_dpad_controller_id_microbit_evt():
    global lastValue
    if lastValue != control.event_value():
        lastValue = control.event_value()
        led.stop_animation()
        if control.event_value() == 1:
            iBIT.set_motor(ibitMotorCH.M1, ibitMotor.FORWARD, 30)
            iBIT.set_motor(ibitMotorCH.M2, ibitMotor.FORWARD, 25)
        elif control.event_value() == 2:
            iBIT.set_motor(ibitMotorCH.M1, ibitMotor.FORWARD, 0)
            iBIT.set_motor(ibitMotorCH.M2, ibitMotor.FORWARD, 0)
        elif control.event_value() == 3:
            iBIT.set_motor(ibitMotorCH.M1, ibitMotor.BACKWARD, 30)
            iBIT.set_motor(ibitMotorCH.M2, ibitMotor.BACKWARD, 25)
        elif control.event_value() == 4:
            iBIT.set_motor(ibitMotorCH.M1, ibitMotor.BACKWARD, 0)
            iBIT.set_motor(ibitMotorCH.M2, ibitMotor.BACKWARD, 0)
        elif control.event_value() == 5:
            iBIT.set_motor(ibitMotorCH.M1, ibitMotor.FORWARD, 30)
        elif control.event_value() == 6:
            iBIT.set_motor(ibitMotorCH.M1, ibitMotor.FORWARD, 0)
        elif control.event_value() == 7:
            iBIT.set_motor(ibitMotorCH.M2, ibitMotor.FORWARD, 25)
        elif control.event_value() == 8:
            iBIT.set_motor(ibitMotorCH.M2, ibitMotor.FORWARD, 0)
        elif control.event_value() == 9:
            basic.show_string("1")
        elif control.event_value() == 10:
            basic.show_string("1 Up")
        elif control.event_value() == 11:
            basic.show_string("2")
        elif control.event_value() == 12:
            basic.show_string("2 Up")
        elif control.event_value() == 13:
            basic.show_string("3")
        elif control.event_value() == 14:
            basic.show_string("3 Up ")
        elif control.event_value() == 15:
            basic.show_string("4")
        elif control.event_value() == 16:
            basic.show_string("4 Up")
        else:
            basic.clear_screen()
control.on_event(EventBusSource.MES_DPAD_CONTROLLER_ID,
    EventBusValue.MICROBIT_EVT_ANY,
    on_mes_dpad_controller_id_microbit_evt)

lastValue = 0
lastValue = 0
bluetooth.start_led_service()
basic.show_icon(IconNames.HEART)