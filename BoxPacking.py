def greedy_by_first_fit(items, boxCapacity):
    # Initialize the list of boxes
    boxes = []

    # Process each item
    for item in items:
        #initializes a flag to track if the item has been placed
        placed = False
        for box in boxes:
            if sum(box) + item <= boxCapacity: # checks if the item can fit in the current box
                box.append(item)
                placed = True
                break
        # if the item didn't fit in any existing box, create a new box
        if not placed:
            new_box = [item]
            boxes.append(new_box)

    return boxes

items = [4, 8, 1, 4, 2, 1]
boxCapacity = 10
packed_boxes = greedy_by_first_fit(items, boxCapacity)
print(f"Packed boxes: {packed_boxes}")