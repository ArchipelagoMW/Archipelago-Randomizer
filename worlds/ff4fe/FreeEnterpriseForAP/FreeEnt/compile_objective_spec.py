import pkgutil
import re
import shutil

CUSTOM_OBJECTIVE_COUNT = 8
objectives = []

with pkgutil.get_data(__name__, "objectivespec.txt").decode().splitlines() as infile:
    next_code = 0x20
    for line in infile:
        line = line.strip()
        if not line or line.startswith('#'):
            continue

        m = re.search(r'^((?P<code>[0-9a-fA-F]{2})\s*:\s*)?(?P<slug>[^\s]+)\s*(?P<text>.*)$', line)
        if not m:
            print(f"Warning: could not interpret line: {line}")
            continue

        if m['code']:
            code = int(m['code'], 16)
        else:
            code = next_code
            next_code += 1

        objectives.append({
            'code' : code,
            'slug' : m['slug'],
            'text' : m['text'],
            'internal' : (m['slug'].startswith('internal_'))
            })

print('Writing objective_data.py')
with open('objective_data.py', 'w') as outfile:
    outfile.write("# This file is auto-generated by compile_objective_spec.py\n")
    outfile.write("OBJECTIVES = {\n")
    for obj in objectives:
        text = obj['text'].replace("'", "\\'")
        outfile.write(f"    0x{obj['code']:02X}: {{'slug' : '{obj['slug']}', 'desc': '{text}'}},\n")
    outfile.write("}\n")

print('Writing scripts/objective_data.f4c')
with open('scripts/objective_data.f4c', 'w') as outfile:
    outfile.write("// This file is auto-generated by compile_objective_spec.py\n")
    outfile.write("consts(objective) {\n")
    outfile.write("  $00  none\n")
    for obj in objectives:
        outfile.write(f"  ${obj['code']:02X}  {obj['slug']}\n")
    outfile.write("}")

print('Updating flagspec')
flagspec_lines = []
with pkgutil.get_data(__name__, "flagspec.txt").decode().splitlines() as infile:
    in_section = False
    for line in infile:
        if 'BEGIN_AUTO_OBJECTIVES' in line:
            in_section = True
            flagspec_lines.append(line)
            slugs = [o['slug'] for o in objectives if not o['internal']]
            for i in range(CUSTOM_OBJECTIVE_COUNT):
                flagspec_lines.append('/'.join([f"O{i+1}:{slug}" for slug in slugs]) + '\n')
        elif 'END_AUTO_OBJECTIVES' in line:
            in_section = False
            flagspec_lines.append(line)
        elif not in_section:
            flagspec_lines.append(line)
shutil.copyfile('flagspec.txt', 'flagspec.txt.backup')
with open('flagspec.txt', 'w') as outfile:
    outfile.write(''.join(flagspec_lines))
print("(don't forget to recompile the flagspec!)")
