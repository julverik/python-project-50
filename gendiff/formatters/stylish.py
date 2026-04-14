def format_value(value, depth=0):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if value == "":
        return '""'
    if isinstance(value, dict):
        indent = '    ' * (depth + 1)
        lines = ['{']
        for k, v in value.items():
            lines.append(f'{indent}    {k}: {format_value(v, depth + 1)}')
        lines.append(f'{indent}}}')
        return '\n'.join(lines)
    return value


def stylish(diff, depth=0):
    indent = '    ' * depth
    lines = ['{']

    for node in diff:
        key = node['key']
        status = node['status']

        if status == 'nested':
            children = stylish(node["children"], depth + 1)
            lines.append(f'{indent}    {key}: {children}')
        elif status == 'added':
            value = format_value(node["value"], depth)
            lines.append(f'{indent}  + {key}: {value}')
        elif status == 'removed':
            value = format_value(node["value"], depth)
            lines.append(f'{indent}  - {key}: {value}')
        elif status == 'unchanged':
            value = format_value(node["value"], depth)
            lines.append(f'{indent}    {key}: {value}')
        elif status == 'changed':
            old_value = format_value(node["old_value"], depth)
            new_value = format_value(node["new_value"], depth)
            lines.append(f'{indent}  - {key}: {old_value}')
            lines.append(f'{indent}  + {key}: {new_value}')

    lines.append(f'{indent}}}')
    return '\n'.join(lines)