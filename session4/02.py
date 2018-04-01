"""
Conditional looping

We used for loop to loop over a list or a range.
We can do that with tuples, similarly.

Now, let us control the operation of an automatic water heater
"""

# turn heater on
heater.turn_on()
# create variable temperature
temperature = 0

# run contents of the loop as long as the condition is met
while temperature < 70:
    # update water temperature
    temperature = heater.measure_water_temperature()

# When the while loop ends, water temperature is 70°
# So turn the heater off
heater.turn_off()

# NOTE: this code will fail, as we don't have a heater defined.
# This is just to explain while loop
