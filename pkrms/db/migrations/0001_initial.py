# Generated by Django 5.1.6 on 2025-04-12 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BridgeInventory',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('year', models.IntegerField(db_column='year')),
                ('admin_code', models.IntegerField(db_column='adminCode')),
                ('link_no', models.CharField(db_column='linkNo', max_length=50)),
                ('bridge_number', models.CharField(db_column='bridgeNumber', max_length=100)),
                ('chainage', models.IntegerField(db_column='chainage')),
                ('drp_from', models.IntegerField(blank=True, db_column='drpFrom', null=True)),
                ('offset_from', models.IntegerField(blank=True, db_column='offsetFrom', null=True)),
                ('bridge_name', models.CharField(db_column='bridgeName', max_length=255)),
                ('bridge_length', models.FloatField(db_column='bridgeLength')),
                ('bridge_type', models.CharField(db_column='bridgeType', max_length=100)),
                ('number_spans', models.FloatField(blank=True, db_column='numberSpans', null=True)),
                ('road_width', models.FloatField(blank=True, db_column='roadWidth', null=True)),
                ('footpath_width_l', models.FloatField(blank=True, db_column='footpathWidthL', null=True)),
                ('footpath_width_r', models.FloatField(blank=True, db_column='footpathWidthR', null=True)),
                ('crossing', models.CharField(blank=True, db_column='crossing', max_length=255, null=True)),
                ('year_construction', models.IntegerField(blank=True, db_column='yearConstruction', null=True)),
                ('bridge_north_deg', models.IntegerField(blank=True, db_column='bridgeNorthDeg', null=True)),
                ('bridge_north_min', models.IntegerField(blank=True, db_column='bridgeNorthMin', null=True)),
                ('bridge_north_sec', models.FloatField(blank=True, db_column='bridgeNorthSec', null=True)),
                ('bridge_east_deg', models.IntegerField(blank=True, db_column='bridgeEastDeg', null=True)),
                ('bridge_east_min', models.IntegerField(blank=True, db_column='bridgeEastMin', null=True)),
                ('bridge_east_sec', models.FloatField(blank=True, db_column='bridgeEastSec', null=True)),
                ('handrails', models.BooleanField(blank=True, db_column='handrails', null=True)),
                ('cond_handrails', models.FloatField(blank=True, db_column='condHandrails', null=True)),
                ('guardrail', models.BooleanField(blank=True, db_column='guardrail', null=True)),
                ('cond_guardrails', models.FloatField(blank=True, db_column='condGuardrails', null=True)),
                ('roadsurface', models.BooleanField(blank=True, db_column='roadsurface', null=True)),
                ('cond_roadsurface', models.FloatField(blank=True, db_column='condRoadsurface', null=True)),
                ('deck', models.BooleanField(blank=True, db_column='deck', null=True)),
                ('cond_deck', models.FloatField(blank=True, db_column='condDeck', null=True)),
                ('deckjoints', models.BooleanField(blank=True, db_column='deckJoints', null=True)),
                ('cond_deckjoints', models.FloatField(blank=True, db_column='condDeckJoints', null=True)),
                ('beam', models.BooleanField(blank=True, db_column='beam', null=True)),
                ('cond_beam', models.FloatField(blank=True, db_column='condBeam', null=True)),
                ('wingwalls', models.BooleanField(blank=True, db_column='wingWalls', null=True)),
                ('cond_wingwalls', models.FloatField(blank=True, db_column='condWingWalls', null=True)),
                ('abutment', models.BooleanField(blank=True, db_column='abutment', null=True)),
                ('cond_abutment', models.FloatField(blank=True, db_column='condAbutment', null=True)),
                ('piers', models.BooleanField(blank=True, db_column='piers', null=True)),
                ('cond_piers', models.FloatField(blank=True, db_column='condPiers', null=True)),
                ('bearings', models.BooleanField(blank=True, db_column='bearings', null=True)),
                ('cond_bearings', models.FloatField(blank=True, db_column='condBearings', null=True)),
                ('foundations', models.BooleanField(blank=True, db_column='foundations', null=True)),
                ('cond_foundations', models.FloatField(blank=True, db_column='condFoundations', null=True)),
                ('stormwaterdrain', models.BooleanField(blank=True, db_column='stormWaterDrain', null=True)),
                ('cond_stormwaterdrain', models.FloatField(blank=True, db_column='condStormWaterDrain', null=True)),
                ('obstruction', models.BooleanField(blank=True, db_column='obstruction', null=True)),
                ('cond_obstruction', models.FloatField(blank=True, db_column='condObstruction', null=True)),
                ('scouring', models.BooleanField(blank=True, db_column='scouring', null=True)),
                ('cond_scouring', models.FloatField(blank=True, db_column='condScouring', null=True)),
                ('analysisbaseyear', models.BooleanField(blank=True, db_column='analysisBaseYear', null=True)),
                ('surveyby', models.CharField(blank=True, db_column='surveyBy', max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Bridge Inventory',
                'verbose_name_plural': 'Bridge Inventories',
                'db_table': 'bridgeinventory',
            },
        ),
        migrations.CreateModel(
            name='CODE_AN_Parameters',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('cumesa1', models.IntegerField(blank=True, db_column='cumesa1', null=True)),
                ('cumesa2', models.IntegerField(blank=True, db_column='cumesa2', null=True)),
                ('profilename', models.CharField(blank=True, db_column='profilename', max_length=100, null=True)),
                ('irif', models.IntegerField(blank=True, db_column='irif', null=True)),
                ('iri_wf', models.IntegerField(blank=True, db_column='iri_wf', null=True)),
                ('surfaceloss_wf', models.IntegerField(blank=True, db_column='surfaceloss_wf', null=True)),
                ('bleeding_wf', models.FloatField(blank=True, db_column='bleeding_wf', null=True)),
                ('ravelling_wf', models.FloatField(blank=True, db_column='ravelling_wf', null=True)),
                ('desintegration_wf', models.IntegerField(blank=True, db_column='desintegration_wf', null=True)),
                ('crackdep_wf', models.IntegerField(blank=True, db_column='crackdep_wf', null=True)),
                ('patching_wf', models.IntegerField(blank=True, db_column='patching_wf', null=True)),
                ('othcrack_wf', models.FloatField(blank=True, db_column='othcrack_wf', null=True)),
                ('pothole_wf', models.FloatField(blank=True, db_column='pothole_wf', null=True)),
                ('rutting_wf', models.FloatField(blank=True, db_column='rutting_wf', null=True)),
                ('edgedamage_wf', models.IntegerField(blank=True, db_column='edgedamage_wf', null=True)),
                ('bleeding_wf_noiri', models.FloatField(blank=True, db_column='bleeding_wf_noiri', null=True)),
                ('ravelling_wf_noiri', models.FloatField(blank=True, db_column='ravelling_wf_noiri', null=True)),
                ('desintegration_wf_noiri', models.IntegerField(blank=True, db_column='desintegration_wf_noiri', null=True)),
                ('crackdep_wf_noiri', models.IntegerField(blank=True, db_column='crackdep_wf_noiri', null=True)),
                ('patching_wf_noiri', models.IntegerField(blank=True, db_column='patching_wf_noiri', null=True)),
                ('othcrack_wf_noiri', models.IntegerField(blank=True, db_column='othcrack_wf_noiri', null=True)),
                ('pothole_wf_noiri', models.FloatField(blank=True, db_column='pothole_wf_noiri', null=True)),
                ('rutting_wf_noiri', models.IntegerField(blank=True, db_column='rutting_wf_noiri', null=True)),
                ('edgedamage_wf_noiri', models.IntegerField(blank=True, db_column='edgedamage_wf_noiri', null=True)),
                ('crossfall_wf', models.FloatField(blank=True, db_column='crossfall_wf', null=True)),
                ('depression_wf', models.FloatField(blank=True, db_column='depression_wf', null=True)),
                ('erosion_wf', models.FloatField(blank=True, db_column='erosion_wf', null=True)),
                ('waviness_wf', models.IntegerField(blank=True, db_column='waviness_wf', null=True)),
                ('gravelthickness_wf', models.IntegerField(blank=True, db_column='gravelthickness_wf', null=True)),
                ('tti_prog_a1', models.FloatField(blank=True, db_column='tti_prog_a1', null=True)),
                ('tti_prog_a2', models.FloatField(blank=True, db_column='tti_prog_a2', null=True)),
                ('tti_prog_a3', models.FloatField(blank=True, db_column='tti_prog_a3', null=True)),
                ('tti_per', models.IntegerField(blank=True, db_column='tti_per', null=True)),
                ('tti_reh', models.IntegerField(blank=True, db_column='tti_reh', null=True)),
                ('tti_max', models.IntegerField(blank=True, db_column='tti_max', null=True)),
                ('tpi_a0', models.IntegerField(blank=True, db_column='tpi_a0', null=True)),
                ('tpi_a1', models.FloatField(blank=True, db_column='tpi_a1', null=True)),
                ('tti_trigger1', models.IntegerField(blank=True, db_column='tti_trigger1', null=True)),
                ('tti_trigger2', models.IntegerField(blank=True, db_column='tti_trigger2', null=True)),
                ('tti_trigger3', models.IntegerField(blank=True, db_column='tti_trigger3', null=True)),
                ('tti_reset_per', models.IntegerField(blank=True, db_column='tti_reset_per', null=True)),
                ('tti_reset_reh', models.IntegerField(blank=True, db_column='tti_reset_reh', null=True)),
            ],
            options={
                'verbose_name': 'Code An Parameters',
                'verbose_name_plural': 'Code An Parameterss',
                'db_table': 'code_an_parameters',
            },
        ),
        migrations.CreateModel(
            name='CODE_AN_UnitCostsPER',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('admin_code', models.IntegerField(blank=True, db_column='adminCode', null=True)),
                ('overlay_thick', models.IntegerField(blank=True, db_column='overlayThick', null=True)),
                ('per_unitcost', models.FloatField(blank=True, db_column='perUnitcost', null=True)),
            ],
            options={
                'verbose_name': 'Code An Unitcostsper',
                'verbose_name_plural': 'Code An Unitcostspers',
                'db_table': 'code_an_unitcostsper',
            },
        ),
        migrations.CreateModel(
            name='CODE_AN_UnitCostsPERUnpaved',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('admin_code', models.IntegerField(blank=True, db_column='adminCode', null=True)),
                ('reg_unitcost', models.FloatField(blank=True, db_column='regUnitcost', null=True)),
                ('res_unitcost', models.FloatField(blank=True, db_column='resUnitcost', null=True)),
            ],
            options={
                'verbose_name': 'Code An Unitcostsperunpaved',
                'verbose_name_plural': 'Code An Unitcostsperunpaveds',
                'db_table': 'code_an_unitcostsperunpaved',
            },
        ),
        migrations.CreateModel(
            name='CODE_AN_UnitCostsREH',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('admin_code', models.IntegerField(blank=True, db_column='adminCode', null=True)),
                ('cumesa1', models.FloatField(blank=True, db_column='cumesa1', null=True)),
                ('cumesa2', models.FloatField(blank=True, db_column='cumesa2', null=True)),
                ('pave_width1', models.FloatField(blank=True, db_column='paveWidth1', null=True)),
                ('pave_width2', models.FloatField(blank=True, db_column='paveWidth2', null=True)),
                ('reh_unitcost', models.FloatField(blank=True, db_column='rehUnitcost', null=True)),
            ],
            options={
                'verbose_name': 'Code An Unitcostsreh',
                'verbose_name_plural': 'Code An Unitcostsrehs',
                'db_table': 'code_an_unitcostsreh',
            },
        ),
        migrations.CreateModel(
            name='CODE_AN_UnitCostsRIGID',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('admin_code', models.IntegerField(blank=True, db_column='adminCode', null=True)),
                ('code', models.IntegerField(blank=True, db_column='code', null=True)),
                ('perunitcost', models.FloatField(blank=True, db_column='perUnitcost', null=True)),
                ('rehunitcost', models.FloatField(blank=True, db_column='rehUnitcost', null=True)),
            ],
            options={
                'verbose_name': 'Code An Unitcostsrigid',
                'verbose_name_plural': 'Code An Unitcostsrigids',
                'db_table': 'code_an_unitcostsrigid',
            },
        ),
        migrations.CreateModel(
            name='CODE_AN_UnitCostsRM',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('admin_code', models.IntegerField(blank=True, db_column='adminCode', null=True)),
                ('rm_activity', models.CharField(blank=True, db_column='rmActivity', max_length=100, null=True)),
                ('terrain', models.IntegerField(blank=True, db_column='terrain', null=True)),
                ('unit', models.CharField(blank=True, db_column='unit', max_length=100, null=True)),
                ('rm_networkelement', models.CharField(blank=True, db_column='rmNetworkElement', max_length=255, null=True)),
                ('rm_category', models.CharField(blank=True, db_column='rmCategory', max_length=100, null=True)),
                ('rm_priority', models.IntegerField(blank=True, db_column='rmPriority', null=True)),
                ('rm_quantity', models.FloatField(blank=True, db_column='rmQuantity', null=True)),
                ('rm_unitcost', models.IntegerField(blank=True, db_column='rmUnitcost', null=True)),
                ('rm_onoff', models.CharField(blank=True, db_column='rmOnoff', max_length=100, null=True)),
                ('rm_reportcategory', models.CharField(blank=True, db_column='rmReportCategory', max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Code An Unitcostsrm',
                'verbose_name_plural': 'Code An Unitcostsrms',
                'db_table': 'code_an_unitcostsrm',
            },
        ),
        migrations.CreateModel(
            name='CODE_AN_UnitCostsUPGUnpaved',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('admin_code', models.IntegerField(blank=True, db_column='adminCode', null=True)),
                ('pave_width1', models.FloatField(blank=True, db_column='paveWidth1', null=True)),
                ('upg_unitcost', models.FloatField(blank=True, db_column='upgUnitcost', null=True)),
            ],
            options={
                'verbose_name': 'Code An Unitcostsupgunpaved',
                'verbose_name_plural': 'Code An Unitcostsupgunpaveds',
                'db_table': 'code_an_unitcostsupgunpaved',
            },
        ),
        migrations.CreateModel(
            name='CODE_AN_UnitCostsWidening',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('admin_code', models.IntegerField(blank=True, db_column='adminCode', null=True)),
                ('cumesa1', models.FloatField(blank=True, db_column='cumesa1', null=True)),
                ('cumesa2', models.FloatField(blank=True, db_column='cumesa2', null=True)),
                ('wideningsealed_unitcost', models.FloatField(blank=True, db_column='wideningSealedUnitcost', null=True)),
                ('wideningunsealed_unitcost', models.FloatField(blank=True, db_column='wideningUnsealedUnitcost', null=True)),
            ],
            options={
                'verbose_name': 'Code An Unitcostswidening',
                'verbose_name_plural': 'Code An Unitcostswidenings',
                'db_table': 'code_an_unitcostswidening',
            },
        ),
        migrations.CreateModel(
            name='CODE_AN_WidthStandards',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('status', models.CharField(blank=True, db_column='status', max_length=100, null=True)),
                ('aadt1', models.IntegerField(blank=True, db_column='aadt1', null=True)),
                ('aadt2', models.IntegerField(blank=True, db_column='aadt2', null=True)),
                ('pave_width', models.FloatField(blank=True, db_column='paveWidth', null=True)),
                ('row', models.IntegerField(blank=True, db_column='row', null=True)),
                ('shldwidth', models.FloatField(blank=True, db_column='shldWidth', null=True)),
                ('minwidening', models.FloatField(blank=True, db_column='minWidening', null=True)),
                ('maxvcr', models.FloatField(blank=True, db_column='maxVcr', null=True)),
            ],
            options={
                'verbose_name': 'Code An Widthstandards',
                'verbose_name_plural': 'Code An Widthstandardss',
                'db_table': 'code_an_widthstandards',
            },
        ),
        migrations.CreateModel(
            name='CulvertCondition',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('year', models.IntegerField(db_column='year')),
                ('admin_code', models.CharField(db_column='adminCode', max_length=100)),
                ('link_no', models.CharField(db_column='linkNo', max_length=50)),
                ('culvert_number', models.CharField(db_column='culvertNumber', max_length=100)),
                ('cond_barrel', models.CharField(blank=True, db_column='condBarrel', max_length=255, null=True)),
                ('cond_inlet', models.CharField(blank=True, db_column='condInlet', max_length=255, null=True)),
                ('cond_outlet', models.CharField(blank=True, db_column='condOutlet', max_length=100, null=True)),
                ('silting', models.CharField(blank=True, db_column='silting', max_length=255, null=True)),
                ('overtopping', models.CharField(blank=True, db_column='overtopping', max_length=100, null=True)),
                ('analysisbaseyear', models.CharField(blank=True, db_column='analysisBaseYear', max_length=255, null=True)),
                ('surveyby', models.CharField(blank=True, db_column='surveyBy', max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Culvertcondition',
                'verbose_name_plural': 'Culvertconditions',
                'db_table': 'culvertcondition',
            },
        ),
        migrations.CreateModel(
            name='CulvertInventory',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('admin_code', models.IntegerField(db_column='adminCode')),
                ('link_no', models.CharField(db_column='linkNo', max_length=50)),
                ('culvert_number', models.CharField(db_column='culvertNumber', max_length=255)),
                ('chainage', models.IntegerField(db_column='chainage')),
                ('drp_from', models.CharField(blank=True, db_column='drpFrom', max_length=255, null=True)),
                ('offset_from', models.CharField(blank=True, db_column='offsetFrom', max_length=255, null=True)),
                ('culvert_length', models.CharField(blank=True, db_column='culvertLength', max_length=255, null=True)),
                ('culvert_type', models.CharField(blank=True, db_column='culvertType', max_length=255, null=True)),
                ('number_opening', models.CharField(blank=True, db_column='numberOpening', max_length=255, null=True)),
                ('culvert_width', models.CharField(blank=True, db_column='culvertWidth', max_length=255, null=True)),
                ('culvert_heigth', models.CharField(blank=True, db_column='culvertHeight', max_length=255, null=True)),
                ('inlet_type', models.CharField(blank=True, db_column='inletType', max_length=255, null=True)),
                ('outlet_type', models.CharField(blank=True, db_column='outletType', max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Culvert Inventory',
                'verbose_name_plural': 'Culvert Inventories',
                'db_table': 'culvertinventory',
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('admin_code', models.IntegerField(blank=True, db_column='adminCode', null=True)),
                ('link_no', models.BigIntegerField(db_column='linkNo')),
                ('link_code', models.IntegerField(db_column='linkCode')),
                ('link_name', models.CharField(db_column='linkName', max_length=255)),
                ('status', models.CharField(blank=True, db_column='status', max_length=255, null=True)),
                ('function', models.CharField(blank=True, db_column='function', max_length=255, null=True)),
                ('class_field', models.FloatField(db_column='class')),
                ('link_length_official', models.FloatField(blank=True, db_column='linkLengthOfficial', null=True)),
                ('link_length_actual', models.FloatField(db_column='linkLengthActual')),
                ('wti', models.IntegerField(blank=True, db_column='wti', null=True)),
                ('mca2', models.IntegerField(blank=True, db_column='mca2', null=True)),
                ('mca3', models.IntegerField(blank=True, db_column='mca3', null=True)),
                ('mca4', models.IntegerField(blank=True, db_column='mca4', null=True)),
                ('mca5', models.IntegerField(blank=True, db_column='mca5', null=True)),
                ('project_number', models.FloatField(blank=True, db_column='projectNumber', null=True)),
                ('cumesa', models.FloatField(blank=True, db_column='cumesa', null=True)),
                ('esa0', models.FloatField(blank=True, db_column='esa0', null=True)),
                ('aadt', models.IntegerField(blank=True, db_column='aadt', null=True)),
                ('accessstatus', models.FloatField(blank=True, db_column='accessStatus', null=True)),
            ],
            options={
                'verbose_name': 'Link',
                'verbose_name_plural': 'Links',
                'db_table': 'link',
            },
        ),
        migrations.CreateModel(
            name='RetainingWallCondition',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('year', models.IntegerField(db_column='year')),
                ('admin_code', models.CharField(db_column='adminCode', max_length=255)),
                ('link_no', models.CharField(db_column='linkNo', max_length=50)),
                ('wall_number', models.CharField(db_column='wallNumber', max_length=255)),
                ('wall_mortar_m2', models.FloatField(blank=True, db_column='wallMortarM2', null=True)),
                ('wall_repair_m3', models.FloatField(blank=True, db_column='wallRepairM3', null=True)),
                ('wall_rebuild_m', models.FloatField(blank=True, db_column='wallRebuildM', null=True)),
                ('analysis_base_year', models.IntegerField(blank=True, db_column='analysisBaseYear', null=True)),
                ('survey_by', models.CharField(blank=True, db_column='surveyBy', max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'RetainingWallCondition',
                'verbose_name_plural': 'RetainingWallConditions',
                'db_table': 'retainingwallcondition',
            },
        ),
        migrations.CreateModel(
            name='RetainingWallInventory',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('admin_code', models.CharField(db_column='adminCode', max_length=255)),
                ('link_no', models.CharField(db_column='linkNo', max_length=50)),
                ('wall_number', models.CharField(blank=True, db_column='wallNumber', max_length=255, null=True)),
                ('wall_side', models.CharField(blank=True, db_column='wallSide', max_length=255, null=True)),
                ('chainagefrom', models.CharField(blank=True, db_column='chainageFrom', max_length=255, null=True)),
                ('drp_from', models.CharField(blank=True, db_column='drpFrom', max_length=255, null=True)),
                ('offset_from', models.CharField(blank=True, db_column='offsetFrom', max_length=255, null=True)),
                ('length', models.CharField(blank=True, db_column='length', max_length=255, null=True)),
                ('wall_material', models.CharField(blank=True, db_column='wallMaterial', max_length=255, null=True)),
                ('wall_height', models.CharField(blank=True, db_column='wallHeight', max_length=255, null=True)),
                ('wall_type', models.CharField(blank=True, db_column='wallType', max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Retainingwallinventory',
                'verbose_name_plural': 'Retainingwallinventorys',
                'db_table': 'retainingwallinventory',
            },
        ),
        migrations.CreateModel(
            name='RoadCondition',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('year', models.IntegerField(db_column='year')),
                ('admin_code', models.IntegerField(db_column='adminCode')),
                ('link_no', models.CharField(db_column='linkNo', max_length=50)),
                ('chainagefrom', models.FloatField(db_column='chainageFrom')),
                ('chainageto', models.FloatField(db_column='chainageTo')),
                ('roughness', models.FloatField(blank=True, db_column='roughness', null=True)),
                ('bleeding_area', models.FloatField(blank=True, db_column='bleedingArea', null=True)),
                ('ravelling_area', models.FloatField(blank=True, db_column='ravellingArea', null=True)),
                ('desintegration_area', models.FloatField(blank=True, db_column='desintegrationArea', null=True)),
                ('crackdep_area', models.FloatField(blank=True, db_column='crackdepArea', null=True)),
                ('patching_area', models.FloatField(blank=True, db_column='patchingArea', null=True)),
                ('othcrack_area', models.FloatField(blank=True, db_column='othcrackArea', null=True)),
                ('pothole_area', models.FloatField(blank=True, db_column='potholeArea', null=True)),
                ('rutting_area', models.FloatField(blank=True, db_column='ruttingArea', null=True)),
                ('edgedamage_area', models.FloatField(blank=True, db_column='edgeDamageArea', null=True)),
                ('crossfall_area', models.FloatField(blank=True, db_column='crossfallArea', null=True)),
                ('depressions_area', models.FloatField(blank=True, db_column='depressionsArea', null=True)),
                ('erosion_area', models.FloatField(blank=True, db_column='erosionArea', null=True)),
                ('waviness_area', models.FloatField(blank=True, db_column='wavinessArea', null=True)),
                ('gravelthickness_area', models.FloatField(blank=True, db_column='gravelThicknessArea', null=True)),
                ('concrete_cracking_area', models.FloatField(blank=True, db_column='concreteCrackingArea', null=True)),
                ('concrete_spalling_area', models.FloatField(blank=True, db_column='concreteSpallingArea', null=True)),
                ('concrete_structuralcracking_area', models.FloatField(blank=True, db_column='concreteStructuralCrackingArea', null=True)),
                ('concrete_cornerbreakno', models.IntegerField(blank=True, db_column='concreteCornerBreakNo', null=True)),
                ('concrete_pumpingno', models.IntegerField(blank=True, db_column='concretePumpingNo', null=True)),
                ('concrete_blowouts_area', models.FloatField(blank=True, db_column='concreteBlowoutsArea', null=True)),
                ('crack_width', models.FloatField(blank=True, db_column='crackWidth', null=True)),
                ('pothole_count', models.IntegerField(blank=True, db_column='potholeCount', null=True)),
                ('rutting_depth', models.FloatField(blank=True, db_column='ruttingDepth', null=True)),
                ('shoulder_l', models.FloatField(blank=True, db_column='shoulderL', null=True)),
                ('shoulder_r', models.FloatField(blank=True, db_column='shoulderR', null=True)),
                ('drain_l', models.FloatField(blank=True, db_column='drainL', null=True)),
                ('drain_r', models.FloatField(blank=True, db_column='drainR', null=True)),
                ('slope_l', models.FloatField(blank=True, db_column='slopeL', null=True)),
                ('slope_r', models.FloatField(blank=True, db_column='slopeR', null=True)),
                ('footpath_l', models.FloatField(blank=True, db_column='footPathL', null=True)),
                ('footpath_r', models.FloatField(blank=True, db_column='footPathR', null=True)),
                ('sign_l', models.FloatField(blank=True, db_column='signL', null=True)),
                ('sign_r', models.FloatField(blank=True, db_column='signR', null=True)),
                ('guidepost_l', models.FloatField(blank=True, db_column='guidePostL', null=True)),
                ('guidepost_r', models.FloatField(blank=True, db_column='guidePostR', null=True)),
                ('barrier_l', models.FloatField(blank=True, db_column='barrierL', null=True)),
                ('barrier_r', models.FloatField(blank=True, db_column='barrierR', null=True)),
                ('roadmarking_l', models.FloatField(blank=True, db_column='roadMarkingL', null=True)),
                ('roadmarking_r', models.FloatField(blank=True, db_column='roadMarkingR', null=True)),
                ('iri', models.FloatField(blank=True, db_column='iri', null=True)),
                ('rci', models.FloatField(blank=True, db_column='rci', null=True)),
                ('analysisbaseyear', models.BooleanField(blank=True, db_column='analysisBaseYear', null=True)),
                ('segmenttti', models.FloatField(blank=True, db_column='segmentTTI', null=True)),
                ('surveyby', models.CharField(blank=True, db_column='surveyBy', max_length=255, null=True)),
                ('paved', models.BooleanField(blank=True, db_column='paved', null=True)),
                ('pavement', models.CharField(blank=True, db_column='pavement', max_length=255, null=True)),
                ('checkdata', models.BooleanField(blank=True, db_column='checkData', null=True)),
                ('composition', models.CharField(blank=True, db_column='composition', max_length=255, null=True)),
                ('cracktype', models.CharField(blank=True, db_column='crackType', max_length=255, null=True)),
                ('potholesize', models.CharField(blank=True, db_column='potholeSize', max_length=255, null=True)),
                ('shouldcond_l', models.CharField(blank=True, db_column='shouldCondL', max_length=255, null=True)),
                ('shouldcond_r', models.CharField(blank=True, db_column='shouldCondR', max_length=255, null=True)),
                ('crossfallshape', models.CharField(blank=True, db_column='crossfallShape', max_length=255, null=True)),
                ('gravelsize', models.CharField(blank=True, db_column='gravelSize', max_length=255, null=True)),
                ('gravelthickness', models.FloatField(blank=True, db_column='gravelThickness', null=True)),
                ('distribution', models.CharField(blank=True, db_column='distribution', max_length=255, null=True)),
                ('edgedamage_area_r', models.FloatField(blank=True, db_column='edgeDamageAreaR', null=True)),
                ('surveyby2', models.CharField(blank=True, db_column='surveyBy2', max_length=255, null=True)),
                ('surveydate', models.CharField(db_column='surveyDate', max_length=50)),
                ('sectionstatus', models.IntegerField(blank=True, db_column='sectionStatus', null=True)),
            ],
            options={
                'verbose_name': 'Road Condition',
                'verbose_name_plural': 'Road Conditions',
                'db_table': 'road_condition',
            },
        ),
        migrations.CreateModel(
            name='RoadInventory',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('admin_code', models.IntegerField(db_column='adminCode')),
                ('link_no', models.CharField(db_column='linkNo', max_length=255)),
                ('chainagefrom', models.IntegerField(db_column='chainageFrom')),
                ('chainageto', models.IntegerField(db_column='chainageTo')),
                ('row', models.IntegerField(db_column='row')),
                ('pave_width', models.FloatField(db_column='paveWidth')),
                ('pave_type', models.IntegerField(db_column='paveType')),
                ('drp_from', models.IntegerField(blank=True, db_column='drpFrom', null=True)),
                ('offset_from', models.IntegerField(blank=True, db_column='offsetFrom', null=True)),
                ('drp_to', models.IntegerField(blank=True, db_column='drpTo', null=True)),
                ('offset_to', models.IntegerField(blank=True, db_column='offsetTo', null=True)),
                ('should_width_l', models.FloatField(blank=True, db_column='shoulderWidthL', null=True)),
                ('should_width_r', models.FloatField(blank=True, db_column='shoulderWidthR', null=True)),
                ('should_type_l', models.IntegerField(blank=True, db_column='shoulderTypeL', null=True)),
                ('should_type_r', models.IntegerField(blank=True, db_column='shoulderTypeR', null=True)),
                ('drain_type_l', models.IntegerField(blank=True, db_column='drainTypeL', null=True)),
                ('drain_type_r', models.IntegerField(blank=True, db_column='drainTypeR', null=True)),
                ('terrain', models.IntegerField(blank=True, db_column='terrain', null=True)),
                ('land_use_l', models.IntegerField(blank=True, db_column='landUseL', null=True)),
                ('land_use_r', models.IntegerField(blank=True, db_column='landUseR', null=True)),
                ('impassable', models.BooleanField(blank=True, db_column='impassable', null=True)),
                ('impassablereason', models.CharField(blank=True, db_column='impassableReason', max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Road Inventory',
                'verbose_name_plural': 'Road Inventories',
                'db_table': 'roadinventory',
            },
        ),
        migrations.CreateModel(
            name='TrafficVolume',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('year', models.IntegerField(blank=True, db_column='year', null=True)),
                ('admin_code', models.IntegerField(db_column='adminCode')),
                ('link_no', models.CharField(db_column='linkNo', max_length=50)),
                ('marketday', models.BooleanField(blank=True, db_column='marketDay', null=True)),
                ('trafficcount', models.CharField(blank=True, db_column='trafficCount', max_length=255, null=True)),
                ('journeytime', models.FloatField(blank=True, db_column='journeyTime', null=True)),
                ('aadt_mc', models.IntegerField(blank=True, db_column='aadtMc', null=True)),
                ('aadt_car', models.IntegerField(blank=True, db_column='aadtCar', null=True)),
                ('aadt_pickup', models.IntegerField(blank=True, db_column='aadtPickup', null=True)),
                ('aadt_microtruck', models.IntegerField(blank=True, db_column='aadtMicroTruck', null=True)),
                ('aadt_small_bus', models.IntegerField(blank=True, db_column='aadtSmallBus', null=True)),
                ('aadt_large_bus', models.IntegerField(blank=True, db_column='aadtLargeBus', null=True)),
                ('aadt_small_truck', models.IntegerField(blank=True, db_column='aadtSmallTruck', null=True)),
                ('aadt_medium_truck', models.IntegerField(blank=True, db_column='aadtMediumTruck', null=True)),
                ('aadt_large_truck', models.IntegerField(blank=True, db_column='aadtLargeTruck', null=True)),
                ('aadt_truck_trailer', models.IntegerField(blank=True, db_column='aadtTruckTrailer', null=True)),
                ('aadt_semi_trailer', models.IntegerField(blank=True, db_column='aadtSemiTrailer', null=True)),
                ('analysisbaseyear', models.BooleanField(blank=True, db_column='analysisBaseYear', null=True)),
                ('surveyby', models.FloatField(blank=True, db_column='surveyBy', null=True)),
            ],
            options={
                'verbose_name': 'Trafficvolume',
                'verbose_name_plural': 'Trafficvolumes',
                'db_table': 'trafficvolume',
            },
        ),
    ]
