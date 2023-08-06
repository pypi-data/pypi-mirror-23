#!/usr/bin/env bash

# Some demo calls of pym-sendevent, for cut-and-paste testing or whatever.

# solr-indexer reindexing started event
pym-sendevent --profile=test --app=solr-indexer \
    --message=message="Starting reindexing process" \
    --message=request="some request" \
    --md-name=logData \
    --metadata=numberOfDocuments=9999 \
    --metadata=thing1="some kind of thing1" \
    --metadata=thing2="some kind of thing2" \
    --metadata=dryRun=False

# An SDM ingestion event
pym-sendevent --profile=test --app=ingestion \
    --exchange=archive.workflow-commands \
    --event=runSdmIngestionWorkflow \
    --key=DSOC.start \
    --message=request="sdm ingestion" \
    --md-name=metadata \
    --metadata=observation=17A-385.sb33768499.eb33853103.57903.23251958333
