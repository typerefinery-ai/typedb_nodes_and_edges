
from loguru import logger
import clean_and_load as clean
import basic_upload as basic
import get_nodes_and_edges as get

typeql = "match $a isa log, has logName 'L1'; "
typeql += "$b isa event, has eventName $c;"
typeql += " $d (owner: $a, item: $b) isa trace, "
typeql += " has traceId $t, has index $f; offset 0; limit 100;"#  get; "

server = {
        "url": 'localhost',
        "port": '1729',
        "database": 'typerefinery',
        "schema": "./schema/alpha.tql"
    }

def try_clean():
    clean.clean_and_load(server)

def try_nodes_edges():
    try_clean()
    get.main(server["url"], server['port'], server["database"], typeql, "webcola.json", logger)



# if this file is run directly, then start here
if __name__ == '__main__':
    try_nodes_edges()