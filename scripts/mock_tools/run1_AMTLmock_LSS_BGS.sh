#!/bin/bash
OUTBASE='/global/cfs/cdirs/desi/survey/catalogs/Y1/mocks/SecondGenMocks/AbacusSummitBGS/altmtl{MOCKNUM}'

#python /pscratch/sd/a/acarnero/codes/LSS/scripts/mock_tools/mkCat_SecondGen_amtl.py --base_output $OUTBASE --mockver ab_secondgen --mocknum $1  --tracer bright --combd y --survey Y1 --add_gtl y --specdata iron --targDir /global/cfs/cdirs/desi/survey/catalogs/Y1/mocks/SecondGenMocks/AbacusSummitBGS --joindspec y 
#python /pscratch/sd/a/acarnero/codes/LSS/scripts/mock_tools/mkCat_SecondGen_amtl.py --base_output $OUTBASE --mockver ab_secondgen --mocknum $1  --tracer BGS_ANY --survey Y1 --add_gtl y --specdata iron --targDir /global/cfs/cdirs/desi/survey/catalogs/Y1/mocks/SecondGenMocks/AbacusSummitBGS --fulld y --fullr y --minr 0 --maxr 18 --use_map_veto '_HPmapcut' --apply_veto y --mkclusran y --nz y --mkclusdat y --splitGC y --outmd 'notscratch' 
#python /pscratch/sd/a/acarnero/codes/LSS/scripts/mock_tools/mkCat_SecondGen_amtl.py --base_output $OUTBASE --mockver ab_secondgen --mocknum $1  --tracer BGS_BRIGHT --survey Y1 --add_gtl y --specdata iron --targDir /global/cfs/cdirs/desi/survey/catalogs/Y1/mocks/SecondGenMocks/AbacusSummitBGS --fulld y --fullr y --minr 0 --maxr 18 --use_map_veto '_HPmapcut' --apply_veto y --mkclusran y --nz y --mkclusdat y --splitGC y --outmd 'notscratch' 
python /pscratch/sd/a/acarnero/codes/LSS/scripts/mock_tools/mkCat_SecondGen_amtl.py --base_output $OUTBASE --mockver ab_secondgen --mocknum $1  --tracer BGS_BRIGHT --survey Y1 --add_gtl y --specdata iron --targDir /global/cfs/cdirs/desi/survey/catalogs/Y1/mocks/SecondGenMocks/AbacusSummitBGS  --minr 0 --maxr 18 --use_map_veto '_HPmapcut'  --mkclusran y --nz y --mkclusdat y --splitGC y --outmd 'notscratch' --ccut -21.55 
