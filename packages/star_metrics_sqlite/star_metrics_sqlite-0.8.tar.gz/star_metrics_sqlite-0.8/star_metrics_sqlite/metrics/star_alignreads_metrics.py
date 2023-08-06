import os

from .metrics_util import get_year
from .metrics_util import get_star_version
from .metrics_util import get_default_parameters
from .metrics_util import get_command_line
from .metrics_util import get_initial_user_parameters
from .metrics_util import get_all_user_parameters
from .metrics_util import get_final_user_redefined_parameters
from .metrics_util import get_final_effective_command_line
from .metrics_util import get_final_parameters_after_user_input
from .metrics_util import get_final_log_out
from .metrics_util import chrlength_txt_tsv_to_df
from .metrics_util import chrnamelength_txt_tsv_to_df
from .metrics_util import chrname_txt_tsv_to_df
from .metrics_util import chrstart_txt_tsv_to_df
from .metrics_util import select_tsv_to_df
from .metrics_util import sjdb_info_txt_tsv_to_df
from .metrics_util import sjdblist_out_tab_tsv_to_df

from .metrics_util import get_genome_generation_parameters
from .metrics_util import get_genome_loading_parameters
from .metrics_util import get_splicing_parameters
from .metrics_util import get_mate_names

import pandas as pd

def star_log_out_to_df(metric_path, engine, run_state, run_uuid, logger):
    df_list = list()
    table_name_list = list()

    year = get_year(metric_path, logger)

    star_version = get_star_version(metric_path, logger)
    star_version_dict = {'version': [star_version]}
    df = pd.DataFrame.from_dict(star_version_dict)
    table_name='star_log_out_version'
    df['run_state'] = run_state
    df['run_uuid'] = run_uuid
    df_list.append(df)
    table_name_list.append(table_name)

    df = get_default_parameters(metric_path, run_uuid, logger)
    if 'outFileNamePrefix' not in df:
        df['outFileNamePrefix'] = None
    table_name='star_log_out_default_parameters'
    df['run_state'] = run_state
    df_list.append(df)
    table_name_list.append(table_name)

    df = get_command_line(metric_path, run_uuid, logger)
    table_name = 'star_log_outcommand_line'
    df['run_state'] = run_state
    df_list.append(df)
    table_name_list.append(table_name)

    df = get_initial_user_parameters(metric_path, run_uuid, logger)
    if 'outFileNamePrefix' not in df:
        df['outFileNamePrefix'] = None
    table_name = 'star_log_out_initial_user_parameters'
    df['run_state'] = run_state
    df_list.append(df)
    table_name_list.append(table_name)

    df = get_all_user_parameters(metric_path, run_uuid, logger)
    if 'outFileNamePrefix' not in df:
        df['outFileNamePrefix'] = None
    if 'outSAMattributes' not in df:
        df['outSAMattributes'] = None
    if 'outSAMattrRGline' not in df:
        df['outSAMattrRGline'] = None
    if 'outSAMheaderHD' not in df:
        df['outSAMheaderHD'] = None
    if 'outSAMmode' not in df:
        df['outSAMmode'] = None
    if 'outSAMunmapped' not in df:
        df['outSAMunmapped'] = None
    if 'limitBAMsortRAM' not in df:
        df['limitBAMsortRAM'] = None
    table_name = 'star_log_out_all_user_parameters'
    df['run_state'] = run_state
    df_list.append(df)
    table_name_list.append(table_name)

    df = get_final_user_redefined_parameters(metric_path, run_uuid, logger)
    if 'outFileNamePrefix' not in df:
        df['outFileNamePrefix'] = None
    if 'outSAMattributes' not in df:
        df['outSAMattributes'] = None
    if 'outSAMattrRGline' not in df:
        df['outSAMattrRGline'] = None
    if 'outSAMheaderHD' not in df:
        df['outSAMheaderHD'] = None
    if 'outSAMmode' not in df:
        df['outSAMmode'] = None
    if 'outSAMunmapped' not in df:
        df['outSAMunmapped'] = None
    if 'limitBAMsortRAM' not in df:
        df['limitBAMsortRAM'] = None
    table_name = 'star_log_out_final_user_redefined_parameters'
    df['run_state'] = run_state
    df_list.append(df)
    table_name_list.append(table_name)

    df = get_final_effective_command_line(metric_path, run_uuid, logger)
    table_name = 'star_log_out_final_effective_command_line'
    df['run_state'] = run_state
    df_list.append(df)
    table_name_list.append(table_name)

    df = final_parameters_after_user_input = get_final_parameters_after_user_input(metric_path, run_uuid, logger)
    table_name = 'star_log_out_final_parameters_after_user_input'
    df['run_state'] = run_state
    df_list.append(df)
    table_name_list.append(table_name)

    df = get_genome_generation_parameters(metric_path, run_uuid, logger)
    table_name = 'star_log_out_genome_generation_parameters'
    df['run_state'] = run_state
    df_list.append(df)
    table_name_list.append(table_name)

    df = get_genome_loading_parameters(metric_path, run_uuid, logger)
    table_name = 'star_log_out_genome_loading_parameters'
    df['run_state'] = run_state
    df_list.append(df)
    table_name_list.append(table_name)

    df = get_splicing_parameters(metric_path, run_uuid, logger)
    table_name = 'star_log_out_splicing_parameters'
    df['run_state'] = run_state
    df_list.append(df)
    table_name_list.append(table_name)

    df = get_mate_names(metric_path, run_uuid, logger)
    table_name = 'star_log_out_mate_names'
    df['run_state'] = run_state
    df_list.append(df)
    table_name_list.append(table_name)

    for i, df in enumerate(df_list):
        table_name = table_name_list[i]
        if df is not None:
            df.to_sql(table_name, engine, if_exists='append')
    return year

def star_log_final_out_to_df(metric_path, engine, year, run_state, run_uuid, logger):
    df = get_final_log_out(metric_path, year, run_uuid, logger)
    table_name = 'star_final_log_out'
    df['run_state'] = run_state
    df.to_sql(table_name, engine, if_exists='append')
    return

def star_sj_out_tab_to_df(metric_path, engine, run_state, run_uuid, logger):
    df = sj_out_tab_tsv_to_df(metric_path, logger)
    table_name = 'star_sj_out_tab'
    df['run_state'] = run_state
    df['run_uuid'] = run_uuid
    df.to_sql(table_name, engine, if_exists='append')
    return

def run_pass_1(run_uuid, engine, logger, metric_name,
               log_final_out_path, log_out_path, sj_out_tab_path):
    run_state = 'pass_1'
    year = star_log_out_to_df(log_out_path, engine, run_state, run_uuid, logger)
    star_log_final_out_to_df(log_final_out_path, engine, year, run_state, run_uuid, logger)
    star_sj_out_tab_to_df(sj_out_tab_path, engine, run_state, run_uuid, logger)
    return

def run_pass_2(run_uuid, engine, logger, metric_name,
               log_final_out_path, log_out_path, sj_out_tab_path):
    run_state = 'pass_2'
    year = star_log_out_to_df(log_out_path, engine, run_state, run_uuid, logger)
    star_log_final_out_to_df(log_final_out_path, engine, year, run_state, run_uuid, logger)
    star_sj_out_tab_to_df(sj_out_tab_path, engine, run_state, run_uuid, logger)
    return
