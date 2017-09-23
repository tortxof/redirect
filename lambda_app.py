import os

from flask import Flask, request, abort, redirect
import boto3

app = Flask(__name__)

app.config['TABLE_NAME'] = os.environ.get('TABLE_NAME')

ddb_client = boto3.client('dynamodb')

@app.route('/')
def index():
    if 'domain' not in request.args:
        abort(400)
    domain = request.args['domain']
    ddb_response = ddb_client.get_item(
        TableName = app.config['TABLE_NAME'],
        Key = {'domain': {'S': domain}},
    )
    if 'Item' in ddb_response:
        return redirect(ddb_response['Item']['redirect']['S'])
    else:
        return abort(404)
