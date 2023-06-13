from flask import jsonify
from src import app


@app.route('/api/foo', methods=['GET'])
def foo():
    """
    Descrição da função foo.
    ---
    parameters:
        - name: parametro1
          in: query
          type: string
          required: true
          description: Descrição do parâmetro 1.
    responses:
        200:
            description: Sucesso.
    """
    return jsonify({'message': 'foo'}), 200

@app.get('/api/foo')
def teste():
    """
    Descrição da função foo.
    ---
    parameters:
        - name: parametro2
        in: query
        type: string
        required: true
        description: Descrição do parâmetro 2.
    responses:
        200:
            description: Sucesso.
    """
    return jsonify({'message': 'teste'}), 200




