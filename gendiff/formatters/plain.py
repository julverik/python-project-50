def format_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, str):
        if value == "":
            return "''"
        return f"'{value}'"
    return value


def plain(diff, parent_key=''):
    lines = []

    for node in diff:
        key = node['key']
        full_key = f"{parent_key}.{key}" if parent_key else key
        status = node['status']

        if status == 'nested':
            lines.append(plain(node['children'], full_key))
        elif status == 'added':
            value = format_value(node['value'])
            lines.append(f"Property '{full_key}' was added with value: {value}")
        elif status == 'removed':
            lines.append(f"Property '{full_key}' was removed")
        elif status == 'changed':
            old_value = format_value(node['old_value'])
            new_value = format_value(node['new_value'])
            msg = (
                f"Property '{full_key}' was updated. "
                f"From {old_value} to {new_value}"
            )
            lines.append(msg)

    return '\n'.join(lines)