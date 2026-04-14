from gendiff.scripts.gendiff import generate_diff


def read_fixture(filename):
    with open(f'tests/fixtures/{filename}', 'r') as f:
        return f.read()


def test_generate_diff_flat_json():
    file1 = 'tests/fixtures/file1_flat.json'
    file2 = 'tests/fixtures/file2_flat.json'
    result = generate_diff(file1, file2)
    expected = read_fixture('result_flat.txt')
    assert result == expected


def test_generate_diff_flat_yaml():
    file1 = 'tests/fixtures/file1_flat.yml'
    file2 = 'tests/fixtures/file2_flat.yml'
    result = generate_diff(file1, file2)
    expected = read_fixture('result_flat.txt')
    assert result == expected


def test_generate_diff_nested_json():
    file1 = 'tests/fixtures/file1_nested.json'
    file2 = 'tests/fixtures/file2_nested.json'
    result = generate_diff(file1, file2)
    expected = read_fixture('result_nested.txt')
    assert result == expected


def test_generate_diff_nested_yaml():
    file1 = 'tests/fixtures/file1_nested.yml'
    file2 = 'tests/fixtures/file2_nested.yml'
    result = generate_diff(file1, file2)
    expected = read_fixture('result_nested.txt')
    assert result == expected