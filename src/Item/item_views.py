from flask import Blueprint, render_template, request, redirect, url_for

from src.Item.item import Item

item_bp = Blueprint('item_blueprint', __name__)

@item_bp.route('/new_item/<sku>/<desc>/<claimed>/<stock>', methods=['POST','GET'])
def new_item(sku, desc, claimed, stock):
    Item(sku, desc, claimed, stock).save_to_mongo()
