from flask import Flask, abort
from flask import jsonify

app = Flask(__name__)


########################################################################
# Data
########################################################################


# contractURI() support

CONTRACT_URI_METADATA = {
    'opensea-creatures': {
        'name': 'OpenSea Creatures',
        'description': 'Friendly creatures of the sea.',
        'image': 'https://example.com/image.png',
        'external_link': 'https://github.com/ProjectOpenSea/opensea-creatures/'
    },
    'opensea-erc1155': {
        'name': 'OpenSea Creature Accessories',
        'description': "Fun and useful accessories for your OpenSea creatures.",
        'image': 'https://example.com/image.png',
        'external_link': 'https://github.com/ProjectOpenSea/opensea-erc1155/'
    }
}
CONTRACT_URI_METADATA_AVAILABLE = CONTRACT_URI_METADATA.keys()


########################################################################
# Routes
########################################################################

# opensea-creatures
@app.route('/api/creature/<token_id>')
def creature(token_id):
    return jsonify({
        'name': 'creature_name',
        'description': 'Friendly OpenSea Creature that enjoys long swims in the ocean.',
        'image': 'image_url',
        'external_url': 'https://openseacreatures.io/%s' % token_id,
        'attributes': 'attributes'
    })


@app.route('/api/box/creature/<token_id>')
def creature_box(token_id):
    return jsonify({
        'name': 'Creature Loot Box',
        'description': 'This lootbox contains some OpenSea Creatures! It can also be traded!',
        'image': 'image_url',
        'external_url': 'https://openseacreatures.io/%s' % token_id,
        'attributes': 'attributes'
    })


@app.route('/api/factory/creature/<token_id>')
def creature_factory(token_id):
    return jsonify({
        'name': name,
        'description': description,
        'image': image_url,
        'external_url': 'https://openseacreatures.io/%s' % token_id,
        'attributes': attributes
    })


# opensea-creatures-accessories

@app.route('/api/accessory/<token_id>')
def accessory(token_id):
    return jsonify({
        'name': 'accessory_name',
        'description': 'A fun and useful accessory for your friendly OpenSea creatures.',
        'image': 'image_url',
        'external_url': 'https://openseacreatures.io/accessory/%s' % token_id,
        'attributes': 'attributes'
    })


@app.route('/api/box/accessory/<token_id>')
def accessory_box(token_id):
    
    return jsonify({
        'name': 'Accessory Loot Box',
        'description': 'This lootbox contains some OpenSea Creature accessories! It can also be traded!',
        'image': 'image_url',
        'external_url': 'https://openseacreatures.io/box/accessory/%s' % token_id,
        'attributes': 'attributes'
    })


@app.route('/api/factory/accessory/<token_id>')
def accessory_factory(token_id):
    return jsonify({
        'name': 'name',
        'description': 'description',
        'image': image_url,
        'external_url': 'https://openseacreatures.io/%s' % token_id,
        'attributes': 'attributes'
    })


# contractURI()

@app.route('/contract/<contract_name>')
def contract_uri(contract_name):
    return jsonify({ contract: "CONTRACT_URI_METADATA[contract_name]"} )


# Error handling
@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404


########################################################################
# Main flow of execution
########################################################################

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
