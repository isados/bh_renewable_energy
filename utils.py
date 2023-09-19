class LineContainerList:
    def __init__(self):
        self.directory = None

    def add(self, container):
        if not self.directory:
            self.directory = [[container]]
            return
        for group in self.directory:
            if self.is_part_of_group(group, container):
                group.append(container)
                return
        self.directory.append([container])

    def __iter__(self):
        return iter(self.directory)
            
    
    @staticmethod
    def is_part_of_group(group, container):
        # print(group[0])
        group_location = group[0].bbox[2] # top part of the group
        new_item_location = container.bbox[2]
        return abs(new_item_location - group_location) < 0.1
    
    def __repr__(self):
        return f'LineContainerList -> {self.directory}'

def turn_into_text(container_group):
    return " ".join([line.get_text() for container in container_group for line in container])