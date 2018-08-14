from flask import Blueprint, render_template, request, redirect, url_for

from src.Item.item import Item

item_bp = Blueprint('item_blueprint', __name__)

@item_bp.route('/new_item/<sku>/<desc>', methods=['POST','GET'])
def new_item(sku, desc):
    Item(sku,desc).save_to_mongo()
