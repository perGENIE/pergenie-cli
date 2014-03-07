#!/usr/bin/env bash

cd test

if [ -d tmp ]; then rm -r tmp ; fi
mkdir tmp

for zyg in CC CG GG NA; do \
    # normal & without rs ID
    for src in .vcf _without_rsID.vcf; do \
        python ../pergenie riskreport \
         -I testcase_rs519113/rs519113_${zyg}${src} \
         -F vcf_whole_genome \
         -O tmp/${zyg}.out \
         -P Asian 1>/dev/null 2>/dev/null

        grep Alz tmp/$zyg.out > tmp/$zyg.Alz.out
        if [ ! "`diff -q tmp/$zyg.Alz.out testcase_rs519113/true.$zyg.Alz.out`" == "" ]; then
            echo $d; exit 1
        fi
    done

    # gzipped
    for src in .vcf.gz; do \
        python ../pergenie riskreport \
         -I testcase_rs519113/rs519113_${zyg}${src} \
         -F vcf_whole_genome \
         -O tmp/${zyg}.out \
         -P Asian \
         --compress gzip 1>/dev/null 2>/dev/null

        grep Alz tmp/$zyg.out > tmp/$zyg.Alz.out
        if [ ! "`diff -q tmp/$zyg.Alz.out testcase_rs519113/true.$zyg.Alz.out`" == "" ]; then
            echo $d; exit 1
        fi
    done
done

rm -r tmp
