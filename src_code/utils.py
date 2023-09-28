ref_dimension = -1
class LineContainerList:
    def __init__(self):
        self.rows = None

    def add(self, container):
        if not self.rows:
            self.rows = [[container]]
            return
        for row in self.rows:
            if self.is_part_of_row(row, container):
                row.append(container)
                return
        self.rows.append([container])

    def __iter__(self):
        return iter(self.rows)
            
    
    @staticmethod
    def is_part_of_row(row, container):
        group_location = row[0].bbox[ref_dimension] # top part of the group
        new_item_location = container.bbox[ref_dimension]
        return abs(new_item_location - group_location) < 2
    
    def __repr__(self):
        return f'LineContainerList -> {self.rows}'

def turn_into_text(rows):
    rows = reorder(rows)
    
    new_rows = []
    for row in rows:
        _tmp_row = [line.get_text() for line in row]
        new_rows.append(_tmp_row)
    new_rows = [separate_items_in_row(row) for row in new_rows]
    return new_rows

def reorder(rows):
    new_rows = []
    for row in rows:
        _tmp_row = sorted(row, key=lambda item: item.bbox[0])
        new_rows.append(_tmp_row)
    return sorted(new_rows, key=lambda row: row[0].bbox[-1], reverse=True)

def separate_items_in_row(row):
    new_row = []
    for item in row:
        new_row.extend(item.strip().split(' '))
    return new_row
        
            


    # return " ".join([line.get_text() for container in row for line in container])
