import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt

# Create a Tkinter window
window = tk.Tk()
window.title("Real-time Pcolormesh Plot")
window.geometry("400x400")

# Create a Figure and Axes objects for plotting
fig, ax = plt.subplots(figsize=(6, 6))
image = ax.pcolormesh([], [], [], cmap='viridis')
fig.colorbar(image)


# Random data generator
def generate_data():
    while True:
        # Generate random data
        data = np.random.rand(10, 10)
        x = np.arange(data.shape[1] + 1)
        y = np.arange(data.shape[0] + 1)

        # Update the plot
        image.set_array(data.flatten())
        image.set_offsets(np.column_stack((x[:-1], y[:-1])).ravel())

        # Redraw the plot
        ax.autoscale()
        fig.canvas.draw()

        # Update the Tkinter window
        window.update()


# Start generating data
generate_data()

# Run the Tkinter event loop
window.mainloop()