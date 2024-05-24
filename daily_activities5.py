import tkinter as tk
from tkinter import messagebox
from collections import deque

class DailyActivity:
    def __init__(self, name, time, place):
        self.name = name
        self.time = time
        self.place = place

class ActivityManager:
    def __init__(self):
        self.activities = deque()

    def add_activity(self, activity):
        self.activities.append(activity)

    def remove_activity(self):
        if self.activities:
            return self.activities.popleft()
        return None

    def get_all_activities(self):
        return list(self.activities)

    def clear_activities(self):
        self.activities.clear()

class ActivityGUI:
    def __init__(self, root, manager):
        self.root = root
        self.manager = manager
        self.root.title("Daily Activities")

        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        self.name_label = tk.Label(self.frame, text="Activity Name:")
        self.name_label.grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(self.frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        self.time_label = tk.Label(self.frame, text="Time:")
        self.time_label.grid(row=1, column=0, padx=5, pady=5)

        self.hours = [f"{i:02d}" for i in range(24)]
        self.minutes = [f"{i:02d}" for i in range(60)]

        self.selected_hour = tk.StringVar(value=self.hours[0])
        self.selected_minute = tk.StringVar(value=self.minutes[0])

        self.hour_menu = tk.OptionMenu(self.frame, self.selected_hour, *self.hours)
        self.hour_menu.grid(row=1, column=1, padx=5, pady=5)

        self.minute_menu = tk.OptionMenu(self.frame, self.selected_minute, *self.minutes)
        self.minute_menu.grid(row=1, column=2, padx=5, pady=5)

        self.place_label = tk.Label(self.frame, text="Place:")
        self.place_label.grid(row=2, column=0, padx=5, pady=5)
        self.place_entry = tk.Entry(self.frame)
        self.place_entry.grid(row=2, column=1, padx=5, pady=5)

        self.add_button = tk.Button(self.frame, text="Add Activity", command=self.add_activity)
        self.add_button.grid(row=3, column=0, pady=10)

        self.clear_button = tk.Button(self.frame, text="Clear List", command=self.clear_list)
        self.clear_button.grid(row=3, column=1, pady=10)

        self.listbox = tk.Listbox(self.frame)
        self.listbox.grid(row=4, columnspan=3, pady=10, padx=5, sticky='we')

        self.show_activities()

    def add_activity(self):
        name = self.name_entry.get()
        hour = self.selected_hour.get()
        minute = self.selected_minute.get()
        place = self.place_entry.get()

        if name and hour and minute and place:
            time = f"{hour}:{minute}"
            activity = DailyActivity(name, time, place)
            self.manager.add_activity(activity)
            messagebox.showinfo("Success", "Activity added successfully!")
            self.clear_entries()
            self.show_activities()
        else:
            messagebox.showwarning("Input Error", "Please fill all fields.")

    def show_activities(self):
        self.listbox.delete(0, tk.END)
        activities = self.manager.get_all_activities()
        for act in activities:
            self.listbox.insert(tk.END, f"{act.name} at {act.time} in {act.place}")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.selected_hour.set(self.hours[0])
        self.selected_minute.set(self.minutes[0])
        self.place_entry.delete(0, tk.END)

    def clear_list(self):
        self.manager.clear_activities()
        self.show_activities()

def main():
    root = tk.Tk()
    manager = ActivityManager()
    gui = ActivityGUI(root, manager)
    root.mainloop()

if __name__ == "__main__":
    main()
