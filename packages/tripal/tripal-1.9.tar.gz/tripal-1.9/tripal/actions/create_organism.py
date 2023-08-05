#!/usr/bin/env python
from __future__ import print_function
import argparse
from tripal import TripalAuth, TripalInstance


class create_organism(object):

    def run(self, args):
        parser = argparse.ArgumentParser(prog=('tripal %s' % self.__class__.__name__), description='Creates an organism into Tripal')
        TripalAuth(parser)
        parser.add_argument("--genus", required=True, help="The genus of the organism")
        parser.add_argument("--species", help="The species of the organism")
        parser.add_argument("--abbr", required=True, help="The abbreviation of the organism")
        parser.add_argument("--common", required=True, help="The common name of the organism")
        parser.add_argument("--description", help="The description of the organism")
        parser.add_argument("--infraspecific-rank", choices=['subspecies', 'varietas', 'subvariety', 'forma', 'subforma'], help="The type name of infraspecific name for any taxon below the rank of species (requires --infraspecific-name.")
        parser.add_argument("--infraspecific-name", help="The infraspecific name for this organism (requires --infraspecific-rank).")

        args = parser.parse_args(args)

        if (args.infraspecific_rank or args.infraspecific_name) and not (args.infraspecific_name and args.infraspecific_rank):
            raise Exception("You should specific both --infraspecific-rank and --infraspecific-name, or none of them.")

        ti = TripalInstance(**vars(args))

        params = {
            'type': 'chado_organism',
            'genus': args.genus,
            'species': args.species,
            'abbreviation': args.abbr,
            'common_name': args.common,
            'description': args.description,
            'type_id': 0,
            'infraspecific_name': '',
        }

        if args.infraspecific_rank:
            params['infraspecific_name'] = args.infraspecific_name
            allowed_ranks = ti.organism.getTaxonomicRanks()

            for r in allowed_ranks:
                if r['name'] == args.infraspecific_rank:
                    params['type_id'] = int(r['cvterm_id'])
                    break

        res = ti.organism.addOrganism(params)

        print("New organism created with Node ID: %s" % res['nid'])
