# Formatting output
print.align  = on       # align fields for readability
print.indent = 2        # indent continuation lines
print.line.length = 512 # set value to be very large to prevent line wrapping

# Sorting
sort = on
sort.format = {author}

# Remove unwanted fields (optional – add or remove as needed)
delete.field {abstract}
delete.field {file}
delete.field {keywords}
delete.field {note}
delete.field {doi}

