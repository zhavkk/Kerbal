import krpc
import time
conn=krpc.connect()
vessel=conn.space_center.active_vessel

vessel.auto_pilot.target_pitch_and_heading(90,90)
vessel.auto_pilot.engage()
vessel.control.throttle = 1
time.sleep(1)
print("launch")
vessel.control.activate_next_stage()
time.sleep(20)
vessel.control.activate_next_stage()
time.sleep(80)
vessel.control.throttle = 0
vessel.auto_pilot.target_pitch_and_heading(0,90)
time.sleep(2)
vessel.control.throttle = 1
