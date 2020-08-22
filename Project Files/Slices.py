class Slice:
    slice_dict = {}

    def __init__(self, name, capacity, new_thresh):
        # initialise attributes
        self.name = name
        self.capacity = capacity
        self.new_thresh = new_thresh
        # self.

    @property
    def slice(self):
        # Pass slice parameters
        self.slice_dict.update({self.name: [self.capacity, self.new_thresh]})
        return self.slice_dict
    

class Slices(Slice):
    def __init__(self, name, capacity, new_thresh, handoff_thresh):
        # inherit from parent class
        super().__init__(name, capacity, new_thresh)
        self.handoff_thresh = handoff_thresh

    @property
    def slice(self):
        # Pass slice parameters
        self.slice_dict.update({self.name: [self.capacity, self.new_thresh, self.handoff_thresh]})
        return self.slice_dict
