import nbformat
import click

notebook = nbformat.v4.new_notebook()

@click.command(help='convert .py to .ipynb')
@click.argument('f', type=click.Path(exists=True), required=True)
@click.argument('t', type=click.Path(), required=True)
def main(f, t):
    _convert(filename=click.format_filename(f))
    _writefile(filename=click.format_filename(t))


def _convert(filename:str):
    code = ''
    with open(file=filename, mode='r', encoding='utf-8') as f:
        for line in f:
            code = code + line
    for cell in code.split(sep=r'# In[ ]:'):
        notebook.cells.append(nbformat.v4.new_code_cell(cell))
    del notebook.cells[0]
    for cell in notebook.cells:
        cell.source = cell.source.strip('\n\n')

def _writefile(filename:str):
    with open(file=filename, mode='w', encoding='utf-8') as f:
        nbformat.write(notebook, fp=filename)
