import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.widgets import Slider, Button, CheckButtons

# Parámetros del modelo
GRID_SIZE = 200
ITERATIONS = 200
MAX_RECOVERY_TIME = 30
MAX_REINFECTIONS = 5
QUARANTINE_THRESHOLD = 100

# Estados posibles
EMPTY = 0
HEALTHY = 1
INFECTED = 2
RECOVERED = 3
DEAD = 4
QUARANTINED = 5

# Crear la cuadrícula inicial
def initialize_grid(size, initial_infected=5):
    grid = np.zeros((size, size), dtype=int)
    grid[1:-1, 1:-1] = HEALTHY
    for _ in range(initial_infected):
        x, y = np.random.randint(1, size-1, size=2)
        grid[x, y] = INFECTED
    return grid

# Reglas de evolución
def update_grid(grid, infection_prob, death_prob, recovery_time, recovery_tracker, reinfection_allowed, reinfection_limit, quarantine_threshold, iteration, reinfection_count):
    new_grid = grid.copy()
    for x in range(1, grid.shape[0] - 1):
        for y in range(1, grid.shape[1] - 1):
            if grid[x, y] == HEALTHY:
                if iteration >= quarantine_threshold:
                    new_grid[x, y] = QUARANTINED
                else:
                    neighbors = grid[x-1:x+2, y-1:y+2]
                    if INFECTED in neighbors:
                        if np.random.rand() < infection_prob:
                            new_grid[x, y] = INFECTED
                            recovery_tracker[x, y] = 0
            elif grid[x, y] == INFECTED:
                recovery_tracker[x, y] += 1
                # Evaluar la probabilidad de muerte cada 4 iteraciones
                if iteration % 4 == 0:
                    if np.random.rand() < death_prob:
                        new_grid[x, y] = DEAD
                    else:
                        # Solo cambiar a RECOVERED si no muere
                        if recovery_tracker[x, y] >= recovery_time:
                            new_grid[x, y] = RECOVERED
            elif reinfection_allowed and grid[x, y] == RECOVERED:
                if reinfection_count[x, y] < reinfection_limit:
                    neighbors = grid[x-1:x+2, y-1:y+2]
                    if INFECTED in neighbors:
                        if np.random.rand() < infection_prob:
                            new_grid[x, y] = INFECTED
                            recovery_tracker[x, y] = 0
                            reinfection_count[x, y] += 1
    return new_grid


# Visualización
def plot_grid(grid, ax):
    cmap = mcolors.ListedColormap(['white', 'green', 'red', 'blue', 'black', 'cyan'])
    bounds = [0, 1, 2, 3, 4, 5, 6]
    norm = mcolors.BoundaryNorm(bounds, cmap.N)
    ax.imshow(grid, cmap=cmap, norm=norm)
    ax.set_title("Simulación Epidemiológica", fontsize=20, fontweight='bold', pad=20)
    ax.axis('off')
    ax.spines['top'].set_visible(True)
    ax.spines['right'].set_visible(True)
    ax.spines['bottom'].set_visible(True)
    ax.spines['left'].set_visible(True)
    for spine in ax.spines.values():
        spine.set_edgecolor('black')
        spine.set_linewidth(2)

# Clase principal
class EpidemicSimulation:
    def __init__(self):
        self.grid = initialize_grid(GRID_SIZE, initial_infected=10)
        self.infection_prob = 0.01
        self.death_prob = 0.0
        self.recovery_time = 5
        self.reinfection_allowed = False
        self.reinfection_limit = MAX_REINFECTIONS
        self.quarantine_threshold = QUARANTINE_THRESHOLD
        self.iterations = ITERATIONS
        self.recovery_tracker = np.zeros_like(self.grid, dtype=int)
        self.reinfection_count = np.zeros_like(self.grid, dtype=int)

        plt.rcParams['font.family'] = 'DejaVu Sans'

        self.fig = plt.figure(figsize=(14, 8))
        self.fig.patch.set_facecolor('#F5F5F5')

        self.ax_simulation = self.fig.add_axes([0.05, 0.1, 0.6, 0.8])
        self.ax_infection = self.fig.add_axes([0.7, 0.8, 0.25, 0.03])
        self.ax_death = self.fig.add_axes([0.7, 0.75, 0.25, 0.03])
        self.ax_recovery = self.fig.add_axes([0.7, 0.7, 0.25, 0.03])
        self.ax_iterations = self.fig.add_axes([0.7, 0.65, 0.25, 0.03])
        self.ax_reinfection_limit = self.fig.add_axes([0.7, 0.6, 0.25, 0.03])
        self.ax_quarantine = self.fig.add_axes([0.7, 0.55, 0.25, 0.03])
        self.ax_reset = self.fig.add_axes([0.7, 0.45, 0.15, 0.07])
        self.ax_reinfection = self.fig.add_axes([0.7, 0.3, 0.2, 0.15])

        # Sliders
        self.slider_infection = Slider(self.ax_infection, 'Infección', 0.0, 1.0, valinit=self.infection_prob, color='red')
        self.slider_death = Slider(self.ax_death, 'Mortalidad', 0.0, 1.0, valinit=self.death_prob, color='black')
        self.slider_recovery = Slider(self.ax_recovery, 'Recuperación', 1, MAX_RECOVERY_TIME, valinit=self.recovery_time, valstep=1, color='blue')
        self.slider_iterations = Slider(self.ax_iterations, 'Iteraciones', 1, 500, valinit=self.iterations, valstep=1, color='gray')
        self.slider_reinfection_limit = Slider(self.ax_reinfection_limit, 'Reinfecciones', 1, 10, valinit=self.reinfection_limit, valstep=1, color='green')
        self.slider_quarantine = Slider(self.ax_quarantine, 'Cuarentena', 0, 500, valinit=self.quarantine_threshold, valstep=1, color='cyan')

        # Botón
        self.btn_reset = Button(self.ax_reset, 'Reiniciar', color='#FFDDC1', hovercolor='#FF5733')
        self.btn_reset.label.set_fontsize(12)
        self.btn_reset.label.set_fontweight('bold')

        # Check button
        self.check_reinfection = CheckButtons(self.ax_reinfection, ['Habilitar Reinfección'], [self.reinfection_allowed])

        # Eventos
        self.slider_infection.on_changed(self.update_sliders)
        self.slider_death.on_changed(self.update_sliders)
        self.slider_recovery.on_changed(self.update_sliders)
        self.slider_iterations.on_changed(self.update_sliders)
        self.slider_reinfection_limit.on_changed(self.update_sliders)
        self.slider_quarantine.on_changed(self.update_sliders)
        self.btn_reset.on_clicked(self.reset_simulation)
        self.check_reinfection.on_clicked(self.toggle_reinfection)

    def update_sliders(self, _):
        self.infection_prob = self.slider_infection.val
        self.death_prob = self.slider_death.val
        self.recovery_time = int(self.slider_recovery.val)
        self.iterations = int(self.slider_iterations.val)
        self.reinfection_limit = int(self.slider_reinfection_limit.val)
        self.quarantine_threshold = int(self.slider_quarantine.val)

    def toggle_reinfection(self, label):
        if label == 'Habilitar Reinfección':
            self.reinfection_allowed = not self.reinfection_allowed

    def reset_simulation(self, _):
        self.grid = initialize_grid(GRID_SIZE, initial_infected=10)
        self.recovery_tracker = np.zeros_like(self.grid, dtype=int)
        self.reinfection_count = np.zeros_like(self.grid, dtype=int)
        self.run_simulation()

    def run_simulation(self):
        for iteration in range(self.iterations):
            self.ax_simulation.clear()
            plot_grid(self.grid, self.ax_simulation)
            self.grid = update_grid(
                self.grid,
                self.infection_prob,
                self.death_prob,
                self.recovery_time,
                self.recovery_tracker,
                self.reinfection_allowed,
                self.reinfection_limit,
                self.quarantine_threshold,
                iteration,
                self.reinfection_count,
            )
            plt.pause(0.1)
        plt.show()

# Ejecutar simulación
sim = EpidemicSimulation()
sim.run_simulation()


    

