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