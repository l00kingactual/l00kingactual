from datetime import datetime
import geological_time
import archaeological_time
import calanders

class Time:
    def __init__(self):

        # Placeholder for Quantum Time
        self.quantum_time = {
            'Planck_time': {'value': 5.391e-44, 'description': 'Smallest meaningful unit of time'}
        }


        # Cosmological time scale
        self.cosmological_time = 13.8e9  # Time since the Big Bang in years
        self.current_epoch = datetime.now()  # Current time in human scale

        # Human time scale
        self.human_time = {
            'year': self.current_epoch.year,
            'month': self.current_epoch.month,
            'day': self.current_epoch.day,
            'hour': self.current_epoch.hour,
            'minute': self.current_epoch.minute,
            'second': self.current_epoch.second
        }




    def set_cosmological_time(self, time_in_years):
        """Set the cosmological time."""
        self.cosmological_time = time_in_years

    def set_human_time(self, year, month, day, hour, minute, second):
        """Set the human time."""
        self.human_time = {
            'year': year,
            'month': month,
            'day': day,
            'hour': hour,
            'minute': minute,
            'second': second
        }

    def get_cosmological_time(self):
        """Get the cosmological time."""
        return self.cosmological_time

    def get_human_time(self):
        """Get the human time."""
        return self.human_time

    def get_archaeological_time(self):
        """Get the archaeological time."""
        return self.archaeological_time

    def get_calendars(self):
        """Get the calendars."""
        return self.calendars
