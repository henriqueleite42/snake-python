initial_pos = 20
block_size = 10

def get_x(position_on_screen, position_in_number):
  total_position = position_on_screen + position_in_number

  if position_on_screen != 0:
    total_position += 3

  top_left_block = (block_size * total_position)

  return initial_pos + top_left_block

def get_y(position_in_number):
  return initial_pos + (block_size * position_in_number)

def get_numbers_to_scoreboard(number, pos):
  x0 = get_x(pos, 0)
  x1 = get_x(pos, 1)
  x2 = get_x(pos, 2)

  y0 = get_y(0)
  y1 = get_y(1)
  y2 = get_y(2)
  y3 = get_y(3)
  y4 = get_y(4)

  numbers = [
    [
      (x0, y0), (x1, y0), (x2, y0),
      (x0, y1),           (x2, y1),
      (x0, y2),           (x2, y2),
      (x0, y3),           (x2, y3),
      (x0, y4), (x1, y4), (x2, y4),
    ],
    [
                (x1, y0),
      (x0, y1), (x1, y1),
                (x1, y2),
                (x1, y3),
      (x0, y4), (x1, y4), (x2, y4),
    ],
    [
      (x0, y0), (x1, y0), (x2, y0),
                          (x2, y1),
      (x0, y2), (x1, y2), (x2, y2),
      (x0, y3),
      (x0, y4), (x1, y4), (x2, y4),
    ],
    [
      (x0, y0), (x1, y0), (x2, y0),
                          (x2, y1),
                (x1, y2), (x2, y2),
                          (x2, y3),
      (x0, y4), (x1, y4), (x2, y4),
    ],
    [
      (x0, y0),           (x2, y0),
      (x0, y1),           (x2, y1),
      (x0, y2), (x1, y2), (x2, y2),
                          (x2, y3),
                          (x2, y4),
    ],
    [
      (x0, y0), (x1, y0), (x2, y0),
      (x0, y1),
      (x0, y2), (x1, y2), (x2, y2),
                          (x2, y3),
      (x0, y4), (x1, y4), (x2, y4),
    ],
    [
      (x0, y0), (x1, y0), (x2, y0),
      (x0, y1),
      (x0, y2), (x1, y2), (x2, y2),
      (x0, y3),           (x2, y3),
      (x0, y4), (x1, y4), (x2, y4),
    ],
    [
      (x0, y0), (x1, y0), (x2, y0),
                          (x2, y1),
                          (x2, y2),
                          (x2, y3),
                          (x2, y4),
    ],
    [
      (x0, y0), (x1, y0), (x2, y0),
      (x0, y1),           (x2, y1),
      (x0, y2), (x1, y2), (x2, y2),
      (x0, y3),           (x2, y3),
      (x0, y4), (x1, y4), (x2, y4),
    ],
    [
      (x0, y0), (x1, y0), (x2, y0),
      (x0, y1),           (x2, y1),
      (x0, y2), (x1, y2), (x2, y2),
                          (x2, y3),
                          (x2, y4),
    ],
  ]

  return numbers[number]
