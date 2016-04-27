import numpy
import math

class DiscreteEnvironment(object):

    def __init__(self, resolution, lower_limits, upper_limits):
        # Store the resolution
        self.resolution = resolution

        # Store the bounds
        self.lower_limits = lower_limits
        self.upper_limits = upper_limits

        # Calculate the dimension
        self.dimension = len(self.lower_limits)

        # Figure out the number of grid cells that are in each dimension
        self.num_cells = self.dimension*[0]
        for idx in range(self.dimension):
            self.num_cells[idx] = numpy.ceil((upper_limits[idx] - lower_limits[idx])/resolution)


    def ConfigurationToNodeId(self, config):
        node_id = 0
        coord=self.ConfigurationToGridCoord(config)
        node_id=self.GridCoordToNodeId(coord)

        return node_id

    def NodeIdToConfiguration(self, nid):
        config = [0] * self.dimension
        coord=self.NodeIdToGridCoord(nid)
        config=self.GridCoordToConfiguration(coord)
        config=numpy.array(config)
        return config

    def ConfigurationToGridCoord(self, config):
        lowBound = self.lower_limits
        upBound = self.upper_limits
        id = []
        for idx, elem in enumerate(config):
            total_dist = upBound[idx] - lowBound[idx]
            percent = (elem-lowBound[idx]) / total_dist
            # calculate the grid length in every dimension
            gridLength = total_dist / self.resolution
            # round to the nearest int and append
            id.append(int(percent*gridLength))
        coord = id
        return coord

    def GridCoordToConfiguration(self, coord):
        lowBound = self.lower_limits
        upBound = self.upper_limits
        config = []
        for idx, elem in enumerate(coord):
            total_dist = upBound[idx] - lowBound[idx]
            total_idx = total_dist / self.resolution
            coordinate_oneD = ((elem+0.5) / total_idx * total_dist) + lowBound[idx]
            config.append(coordinate_oneD)
        return config


    def GridCoordToNodeId(self,coord):
        node_id = coord[0]
        for idx in range(1, self.dimension):
            val = 1
            for i in range(idx):
                val = self.num_cells[i]*val
            node_id = node_id + (coord[idx] * val)
        node_id=int(node_id)
        return node_id

    def NodeIdToGridCoord(self, node_id):
        coord = [0] * self.dimension
        val = 1
        for i in range(self.dimension-1):
            val = val * self.num_cells[i]
        for idx in range(self.dimension-1,0,-1):
            coord[idx] = int(numpy.floor(node_id / val))
            node_id = int(node_id%val)
            val = val / self.num_cells[idx-1]
        coord[0] = node_id
        return coord

