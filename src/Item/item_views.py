from flask import Blueprint, render_template, request, redirect, url_for, make_response

from src.Item.item import Item

item_bp = Blueprint('item_blueprint', __name__)

@item_bp.route('/new_item/<sku>/<desc>/<claimed>/<stock>', methods=['POST','GET'])
def new_item(sku, desc, claimed, stock):
    Item(sku, desc, claimed, stock).save_to_mongo()

@item_bp.route('/search_item/<id>', methods=['GET'])
def search_item(id):
    id = id[-4:]
    item = Item.get_by_sku(id)
    make_response(item.json())