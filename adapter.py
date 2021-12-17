class MappingAdapter:
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def lighten(self, grid):
        self.adaptee.set_dim([len(grid[0]), len(grid)])
        lights = self._get_coord_from_grid(grid, 1)
        walls = self._get_coord_from_grid(grid, -1)
        self.adaptee.set_lights(lights)
        self.adaptee.set_obstacles(walls)
        return self.adaptee.generate_lights()

    @staticmethod
    def _get_coord_from_grid(grid, value):
        return [[j, i] for i, i_val in enumerate(grid) for j, j_val in enumerate(i_val) if j_val == value]
