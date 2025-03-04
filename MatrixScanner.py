import MuxDriver as m
import pinmap_rp2 as p

# rows 3-7 will be included later
rows = [p.row1, p.row2]

inputs = []


def scan_matrix():
    for i in range(len(rows)):
        rows[i].value(1)
        for j in range(8):
            if m.read_mux(j) == 1:
                inputs.append([i, j])
