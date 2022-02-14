#!/usr/bin/env python3.9
from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import yaml, json, sys, os




f = open('inventoryoutput.json')

data = json.load(f)


def findhosts():
    all_host_test=[]
    all_host_prod=[]
    all_host=['mcc_apache_website_prod', 'gaar', 'ularda', 'balut', 'gammu', 'buzzell', 'ginaz', 'tleilax', 'gw01', 'gw03', 'cnr_gateway', 'axa_gateway', 'eramet_gateway', 'capgemini_gateway', 'fnacdarty_gateway', 'mcc_gateway', 'mccdev-gateway', 'technicolor-gateway', 'andros-gateway', 'reworld-gateway', 'thales-restore-gateway', 'orangecss-gateway', 'april-gateway', 'lagarderetr-gateway', 'kering-gateway', 'prosol-gateway', 'wazuh-prod', 'epi-dia-prod', 'eli-dia-prod', 'ipsndiaprod', 'ipsnoraprod', 'bvdiaprod', 'bvoraprod2', 'epi_ora_prod_new', 'eli_ora_prod_new', 'cudiaprod', 'taepi', 'cristalunion_ora_prod', 'bureauveritas_ora_prod', 'ipsen_ora_prod', 'WWWHSTDBY', 'ars_dia_prod', 'ars_ora_prod', 'saf_web', 'finae_dia_prod', 'mesit_dia_prod', 'saf_ora_prod', 'saf_sftp', 'areas_sftp', 'areas_web', 'thales_ora_prod', 'thales_sftp_prod', 'thales_dia_prod', 'thales_apache_prod', 'eureden_dia_prod', 'eureden_ora_prod', 'eureden_apache_prod', 'eureden_sftp_prod', 'decathlon_ora_prod', 'decathlon_dia_prod', 'decathlon_apache_prod', 'decathlon_sftp_prod', 'cooperl_ora_prod', 'cooperl_dia_prod', 'cooperl_apache_prod', 'cooperl_sftp_prod', 'teleperformance_ora_prod', 'teleperformance_apache_prod', 'teleperformance_dia_prod', 'decathlon_ipsec_prod', 'econocom_ora_prod', 'econocom_dia_prod', 'econocom_apache_prod', 'bompard_dia_prod', 'bompard_ora_prod', 'bompard_apache_prod', 'capgemini01_prod', 'pcvs', 'pdxecfao', 'fpweb', 'fneofiprod', 'ecnoraprod', 'capgemini02-prod', 'ecn_al2_prod', 'econoal3-backup', 'fidrys-prod3', 'fidrys-prod4', 'ecn_al2_drp', 'apache_www', 'fidrys-prod2', 'capgemini_ora_prod_live', 'ecncm-prod', 'cnr_dia_prod', 'cnr_sftp_prod', 'cnr_apache_prod', 'cnr_ora_prod', 'axa_apache_prod', 'eramet_ora_prod', 'eramet_dia_prod', 'eramet_apache_prod', 'eramet_sftp_prod', 'capgemini_ora_prod', 'capgemini_dia_prod', 'capgemini_sftp_prod', 'capgemini_apache_prod', 'fnacdarty_apache_prod', 'fnacdarty_dia_prod', 'fnacdarty_sftp_prod', 'fnacdarty_ora_prod', 'wazuh-dev', 'technicolor-apache-prod', 'technicolor-ora-prod', 'technicolor-dia-prod', 'andros-ora-prod', 'andros-sftp-prod', 'andros-apache-prod', 'andros-dia-prod', 'reworld_dia_prod', 'reworld_ora_prod', 'reworld_sftp_prod', 'reworld_apache_prod', 'orangecss_dia_prod', 'orangecss_sftp_prod', 'orangecss_ora_prod', 'orangecss_apache_prod', 'thales-restore-ora-prod', 'thales-restore-dia-prod', 'thales-restore-apache-prod', 'thales-restore-sftp-prod', 'april-dia-prod', 'april-apache-prod', 'april-ora-prod', 'april-sftp-prod', 'lagarderetr-dia-prod', 'lagarderetr-ora-prod', 'lagarderetr-sftp-prod', 'lagarderetr-apache-prod', 'kering-apache-prod', 'kering-sftp-prod', 'kering-ora-prod', 'kering-dia-prod', 'prosol-apache-prod', 'prosol-sftp-prod', 'prosol-ora-prod', 'rsg_oracle', 'epi_neptune_dev', 'elidiaorat', 'ipsn_dia_ora_t', 'bvdiaorat', 'cu-dia-ora-test', 'tabneptune', 'bv_ora_test', 'ars_dia_test', 'ars_ora_test', 'finae_dia_test', 'mesit_dia_test', 'saf_ora_test', 'finae_dia_test_temp', 'saf_dia_test_temp', 'saf_web', 'saf_sftp', 'areas_web', 'decathlon_ora_test', 'wavestone_dia_test', 'wavestone_ora_test', 'wavestone_apache_test', 'wavestone_sftp_test', 'thales_ora_test', 'thales_dia_test', 'thales_sftp_prod', 'thales_apache_prod', 'eureden_apache_prod', 'eureden_dia_ora_test', 'decathlon_apache_prod', 'cooperl_ora_test', 'cooperl_dia_test', 'cooperl_apache_prod', 'cooperl_sftp_prod', 'teleperformance_ora_test', 'teleperformance_dia_test', 'teleperformance_apache_prod', 'econocom_ora_test', 'econocom_dia_test', 'decathlon_dia_test', 'bompard_dia_test', 'bompard_ora_test', 'bompard_apache_prod', 'oracle_linux_db19', 'captrans', 'cfao-test', 'fidrystest', 'fidrystest2', 'ecn_al2_test', 'fidrys-prod5', 'ecncmt2', 'cnr_dia_test', 'cnr_ora_test', 'axa_dia_test', 'axa_apache_prod', 'axa_ora_test', 'eramet_ora_test', 'eramet_dia_test', 'eramet_apache_prod', 'capgemini_dia_test', 'capgemini_ora_test', 'fnacdarty_apache_prod', 'fnacdarty_dia_test', 'fnacdarty_ora_test', 'mccdev-dia-test', 'technicolor-ora-test', 'technicolor-dia-test', 'technicolor-apache-prod', 'andros-ora-test', 'andros-apache-prod', 'andros-dia-test', 'reworld_dia_test', 'reworld_ora_test', 'reworld_apache_prod', 'orangecss_dia_test', 'orangecss_sftp_prod', 'orangecss_ora_prod', 'orangecss_apache_prod', 'orangecss_ora_test', 'thales-restore-ora-test', 'thales-restore-dia-test', 'april-dia-test', 'april-apache-prod', 'april-ora-test', 'lagarderetr-dia-test', 'lagarderetr-ora-test', 'lagarderetr-apache-prod', 'kering-dia-test', 'kering-ora-test', 'prosol-dia-test', 'prosol-ora-test']
    for u in data['env_test']['hosts']:
        all_host_test.append(u)
    # print (all_host_test)
    for p in data['env_prod']['hosts']:
        all_host_prod.append(p)
    # print (all_host_prod)
    # all_host= all_host_prod+all_host_test
    print (all_host)



    st.write('apllication')

    host = st.selectbox(
    'select one from the list',
    (all_host)
    )

    st.write('you selected:', host)




findhosts()
