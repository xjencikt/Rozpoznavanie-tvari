import os
import numpy as np
import csv
from PIL import Image
from deepface import DeepFace

def get_image_paths(root_dirs):
    image_paths = []

    for root_dir in root_dirs:
        for root, dirs, files in os.walk(root_dir):
            for file in files:
                if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
                    image_path = os.path.join(root, file)
                    image_paths.append((root, file, image_path))

    return image_paths


root_dirs = ['Karin_Viard_1', 'Karin_Viard_3', 'Katalin_Kollat_2', 'Katalin_Kollat_4', 'Kate_Capshaw_4', 'Kate_Capshaw_1', 'Kate_Winslet_1', 'Kate_Winslet_0', 'Katharine_Hepburn_4', 'Katharine_Hepburn_3', 'Kathryn_Morris_4', 'Kathryn_Morris_5', 'Kathryn_Morris_4', 'Kathryn_Morris_1', 'Katja_Riemann_1', 'Katja_Riemann_0', 'Keira_Knightley_3', 'Keira_Knightley_1', 'Keith_Olbermann_0', 'Keith_Olbermann_2', 'Keith_Olbermann_0', 'Keith_Olbermann_1', 'Keith_Tyson_1', 'Keith_Tyson_2', 'Kelsey_Grammer_1', 'Kelsey_Grammer_4', 'Kemal_Dervis_1', 'Kemal_Dervis_0', 'Kenneth_Branagh_3', 'Kenneth_Branagh_5', 'Kenneth_Carlsen_3', 'Kenneth_Carlsen_4', 'Kenneth_Reichert_3', 'Kenneth_Reichert_2', 'Kevin_Borseth_0', 'Kevin_Borseth_2', 'Kevin_Satterfield_0', 'Kevin_Satterfield_2', 'Kevin_Spacey_1', 'Kevin_Spacey_0', 'Kevin_Spacey_1', 'Kevin_Spacey_2', 'Kieran_Culkin_1', 'Kieran_Culkin_0', 'Kim_Cattrall_0', 'Kim_Cattrall_4', 'Kim_Gandy_0', 'Kim_Gandy_3', 'Kim_Gandy_0', 'Kim_Gandy_4', 'King_Abdullah_II_1', 'King_Abdullah_II_4', 'Kirk_Ferentz_4', 'Kirk_Ferentz_5', 'Kirk_Ferentz_4', 'Kirk_Ferentz_2', 'Kirsten_Dunst_3', 'Kirsten_Dunst_0', 'Kit_Bond_5', 'Kit_Bond_2', 'Kit_Bond_5', 'Kit_Bond_1', 'Kofi_Annan_2', 'Kofi_Annan_3', 'Kostya_Tszyu_1', 'Kostya_Tszyu_2', 'Krishna_Bhadur_Mahara_5', 'Krishna_Bhadur_Mahara_3', 'Kristen_Breitweiser_2', 'Kristen_Breitweiser_0', 'Kristen_Breitweiser_2', 'Kristen_Breitweiser_1', 'Kristin_Chenoweth_1', 'Kristin_Chenoweth_5', 'Kristin_Scott_5', 'Kristin_Scott_1', 'Kristy_Curry_2', 'Kristy_Curry_3', 'Kurt_Warner_4', 'Kurt_Warner_0', 'Kweisi_Mfume_0', 'Kweisi_Mfume_5', 'Kweisi_Mfume_0', 'Kweisi_Mfume_4', 'Kyle_Shewfelt_4', 'Kyle_Shewfelt_2', 'Kyle_Shewfelt_4', 'Kyle_Shewfelt_1', 'Larry_Brown_2', 'Larry_Brown_1', 'Larry_Flynt_1', 'Larry_Flynt_2', 'Larry_Nichols_0', 'Larry_Nichols_1', 'Larry_Wilmore_2', 'Larry_Wilmore_0', 'Laura_Bozzo_4', 'Laura_Bozzo_1', 'Laura_Bush_2', 'Laura_Bush_4', 'Laura_Bush_2', 'Laura_Bush_1', 'Laura_Elena_Harring_2', 'Laura_Elena_Harring_0', 'Laura_Elena_Harring_2', 'Laura_Elena_Harring_4', 'Laura_Flessel_2', 'Laura_Flessel_0', 'Laura_Linney_0', 'Laura_Linney_4', 'Laura_Pausini_0', 'Laura_Pausini_2', 'Lauren_Hutton_5', 'Lauren_Hutton_0', 'Lauren_Hutton_5', 'Lauren_Hutton_4', 'Laurence_Fishburne_2', 'Laurence_Fishburne_5', 'Laurence_Tribe_0', 'Laurence_Tribe_5', 'Laurie_Laychak_0', 'Laurie_Laychak_4', 'Lee_Baca_4', 'Lee_Baca_0', 'Lee_Byung-woong_0', 'Lee_Byung-woong_5', 'Leland_Chapman_4', 'Leland_Chapman_1', 'Lena_Olin_1', 'Lena_Olin_0', 'Lene_Espersen_1', 'Lene_Espersen_2', 'Leonid_Kuchma_2', 'Leonid_Kuchma_4', 'Lesia_Burlak_3', 'Lesia_Burlak_0', 'Lester_Holt_0', 'Lester_Holt_3', 'Leszek_Miller_3', 'Leszek_Miller_1', 'Leticia_Dolera_4', 'Leticia_Dolera_2', 'Leticia_Van_de_Putte_0', 'Leticia_Van_de_Putte_4', 'Leuris_Pupo_4', 'Leuris_Pupo_0', 'Leuris_Pupo_4', 'Leuris_Pupo_3', 'Lewis_Booth_2', 'Lewis_Booth_0', 'Li_Zhaoxing_0', 'Li_Zhaoxing_4', 'Liane_Janda_1', 'Liane_Janda_4', 'Lin_Yung_Hsi_3', 'Lin_Yung_Hsi_4', 'Lincoln_Chafee_2', 'Lincoln_Chafee_5', 'Linda_Dano_2', 'Linda_Dano_5', 'Linda_Dano_2', 'Linda_Dano_3', 'Linda_Franklin_2', 'Linda_Franklin_0', 'Linda_Franklin_2', 'Linda_Franklin_4', 'Linda_Lingle_4', 'Linda_Lingle_2', 'Linda_Mason_5', 'Linda_Mason_4', 'Linda_Sanchez_2', 'Linda_Sanchez_0', 'Linda_Sanchez_2', 'Linda_Sanchez_1', 'Lindsey_Graham_1', 'Lindsey_Graham_0', 'Lindsey_Graham_1', 'Lindsey_Graham_3', 'Lino_Oviedo_5', 'Lino_Oviedo_0', 'Lisa_Leslie_3', 'Lisa_Leslie_5', 'Lisa_Ling_0', 'Lisa_Ling_2', 'Lisa_Marie_Presley_1', 'Lisa_Marie_Presley_2', 'Liu_Mingkang_0', 'Liu_Mingkang_1', 'Liu_Ye_5', 'Liu_Ye_2', 'Liu_Ye_5', 'Liu_Ye_0', 'Liv_Tyler_3', 'Liv_Tyler_5', 'Loretta_Lynn_Harper_4', 'Loretta_Lynn_Harper_3', 'Loretta_Lynn_Harper_4', 'Loretta_Lynn_Harper_0', 'Lorraine_Bracco_5', 'Lorraine_Bracco_0', 'Lou_Lang_5', 'Lou_Lang_0', 'Louis_Van_Gaal_1', 'Louis_Van_Gaal_0', 'Louisa_Baileche_2', 'Louisa_Baileche_0', 'Lubomir_Zaoralek_2', 'Lubomir_Zaoralek_5', 'Luc_Montagnier_2', 'Luc_Montagnier_5', 'Lucia_Kenny_Anthony_1', 'Lucia_Kenny_Anthony_4', 'Lucia_Kenny_Anthony_1', 'Lucia_Kenny_Anthony_5', 'Lucio_Stanca_0', 'Lucio_Stanca_4', 'Lucio_Stanca_0', 'Lucio_Stanca_2', 'Ludivine_Sagnier_3', 'Ludivine_Sagnier_0', 'Luis_Ernesto_Derbez_Bautista_0', 'Luis_Ernesto_Derbez_Bautista_5', 'Luis_Fonsi_4', 'Luis_Fonsi_2', 'Luiz_Inacio_Lula_da_Silva_4', 'Luiz_Inacio_Lula_da_Silva_2', 'Lyle_Lovett_5', 'Lyle_Lovett_4', 'Lynne_Cheney_0', 'Lynne_Cheney_1', 'Mack_Brown_4', 'Mack_Brown_5', 'Madeleine_Albright_3', 'Madeleine_Albright_5', 'Maggie_Cheung_5', 'Maggie_Cheung_0', 'Maggie_Smith_4', 'Maggie_Smith_0', 'Mahathir_Mohamad_1', 'Mahathir_Mohamad_3', 'Mahathir_Mohamad_1', 'Mahathir_Mohamad_0', 'Mahmoud_Abbas_5', 'Mahmoud_Abbas_1', 'Malcolm_Jamal_Warner_2', 'Malcolm_Jamal_Warner_1', 'Manijeh_Hekmat_0', 'Manijeh_Hekmat_2', 'Manuel_Llorente_3', 'Manuel_Llorente_0', 'Manuel_Pellegrini_2', 'Manuel_Pellegrini_3', 'Marc_Anthony_5', 'Marc_Anthony_2', 'Marc_Bulger_1', 'Marc_Bulger_0', 'Marc_Racicot_4', 'Marc_Racicot_2', 'Marc_Racicot_4', 'Marc_Racicot_0', 'Marc_Shaiman_3', 'Marc_Shaiman_1', 'Marcos_Milinkovic_2', 'Marcos_Milinkovic_0', 'Margaret_Thatcher_1', 'Margaret_Thatcher_4', 'Margaret_Thatcher_1', 'Margaret_Thatcher_3', 'Maria_Bello_5', 'Maria_Bello_3', 'Maria_Bello_5', 'Maria_Bello_4', 'Maria_Callas_1', 'Maria_Callas_2', 'Maria_Guida_0', 'Maria_Guida_3', 'Maria_Shriver_4', 'Maria_Shriver_0', 'Maria_Soledad_Alvear_Valenzuela_1', 'Maria_Soledad_Alvear_Valenzuela_3', 'Mariana_Ohata_0', 'Mariana_Ohata_3', 'Marie-Josee_Croze_3', 'Marie-Josee_Croze_4', 'Marieta_Chrousala_4', 'Marieta_Chrousala_0', 'Marina_Silva_5', 'Marina_Silva_2', 'Marina_Silva_5', 'Marina_Silva_4', 'Mario_Cipollini_5', 'Mario_Cipollini_1', 'Mario_Dumont_2', 'Mario_Dumont_0', 'Mario_Gallegos_3', 'Mario_Gallegos_4', 'Mario_Kreutzberger_4', 'Mario_Kreutzberger_3', 'Mario_Lobo_Zagallo_5', 'Mario_Lobo_Zagallo_1', 'Marisa_Tomei_1', 'Marisa_Tomei_4', 'Marissa_Jaret_Winokur_4', 'Marissa_Jaret_Winokur_3', 'Mark_Cuban_3', 'Mark_Cuban_4', 'Mark_Dacey_0', 'Mark_Dacey_3', 'Mark_Foley_5', 'Mark_Foley_4', 'Mark_Geragos_2', 'Mark_Geragos_4', 'Mark_Kelly_0', 'Mark_Kelly_1', 'Mark_Leno_2', 'Mark_Leno_1', 'Mark_Wahlberg_2', 'Mark_Wahlberg_3', 'Martha_Lucia_Ramirez_2', 'Martha_Lucia_Ramirez_3', 'Martin_Landau_0', 'Martin_Landau_2', 'Martin_Luther_King_III_0', 'Martin_Luther_King_III_3', 'Martin_McGuinness_4', 'Martin_McGuinness_1', 'Martin_Sheen_5', 'Martin_Sheen_4', 'Martin_Sheen_5', 'Martin_Sheen_3', 'Mary_Carey_4', 'Mary_Carey_0', 'Mary_Landrieu_3', 'Mary_Landrieu_2', 'Mary_Matalin_2', 'Mary_Matalin_5', 'Mary_Matalin_2', 'Mary_Matalin_3', 'Mary_Robinson_4', 'Mary_Robinson_2', 'Mary_Robinson_4', 'Mary_Robinson_5', 'Massoud_Barzani_0', 'Massoud_Barzani_1', 'Massoud_Barzani_0', 'Massoud_Barzani_4', 'Matt_Anderson_0', 'Matt_Anderson_2', 'Matt_LeBlanc_0', 'Matt_LeBlanc_3', 'Nadia_Petrova_4', 'Nadia_Petrova_5', 'Nadine_Vinzens_0', 'Nadine_Vinzens_4', 'Nancy_Kerrigan_3', 'Nancy_Kerrigan_2', 'Nancy_Kerrigan_3', 'Nancy_Kerrigan_4', 'Nancy_Pelosi_4', 'Nancy_Pelosi_0', 'Nancy_Reagan_1', 'Nancy_Reagan_3', 'Nancy_Reagan_1', 'Nancy_Reagan_4', 'Nanni_Moretti_4', 'Nanni_Moretti_2', 'Narendra_Modi_2', 'Narendra_Modi_3', 'Narendra_Modi_2', 'Narendra_Modi_4', 'Natalia_Verbeke_5', 'Natalia_Verbeke_3', 'Natalia_Vodonova_0', 'Natalia_Vodonova_2', 'Natalie_Cole_5', 'Natalie_Cole_2', 'Natalie_Coughlin_5', 'Natalie_Coughlin_2', 'Natalie_Imbruglia_1', 'Natalie_Imbruglia_2', 'Natalie_Stewart_2', 'Natalie_Stewart_3', 'Natasa_Micic_0', 'Natasa_Micic_5', 'Natasha_Henstridge_3', 'Natasha_Henstridge_1', 'Natasha_Lyonne_4', 'Natasha_Lyonne_0', 'Natasha_McElhone_4', 'Natasha_McElhone_1', 'Nathan_Lane_1', 'Nathan_Lane_0', 'Newt_Gingrich_4', 'Newt_Gingrich_2', 'Newt_Gingrich_4', 'Newt_Gingrich_1', 'Nia_Vardalos_2', 'Nia_Vardalos_1', 'Nicanor_Duarte_Frutos_2', 'Nicanor_Duarte_Frutos_0', 'Nicanor_Duarte_Frutos_2', 'Nicanor_Duarte_Frutos_5', 'Nick_Markakis_3', 'Nick_Markakis_2', 'Nick_Nolte_2', 'Nick_Nolte_5', 'Nick_Reilly_1', 'Nick_Reilly_5', 'Nick_Rimando_3', 'Nick_Rimando_2', 'Nicolas_Cage_0', 'Nicolas_Cage_1', 'Nicolas_Eyzaguirre_2', 'Nicolas_Eyzaguirre_0', 'Nicolas_Sarkozy_1', 'Nicolas_Sarkozy_2', 'Nicolas_Sarkozy_1', 'Nicolas_Sarkozy_5', 'Nikki_McKibbin_0', 'Nikki_McKibbin_5', 'Nina_Jacobson_3', 'Nina_Jacobson_0', 'Noel_Niell_1', 'Noel_Niell_4', 'Nona_Gaye_4', 'Nona_Gaye_5', 'Nora_Ephron_4', 'Nora_Ephron_1', 'Norah_Jones_5', 'Norah_Jones_4', 'Norah_Jones_5', 'Norah_Jones_2', 'Norm_Macdonald_1', 'Norm_Macdonald_4', 'Norm_Macdonald_1', 'Norm_Macdonald_5', 'Norman_Mineta_0', 'Norman_Mineta_5', 'Nuon_Chea_1', 'Nuon_Chea_0', 'Nursultan_Nazarbayev_1', 'Nursultan_Nazarbayev_3', 'Olene_Walker_4', 'Olene_Walker_1', 'Olene_Walker_4', 'Olene_Walker_0', 'Oliver_Phelps_0', 'Oliver_Phelps_2', 'Olivia_Newton-John_0', 'Olivia_Newton-John_4', 'Olympia_Dukakis_1', 'Olympia_Dukakis_4', 'Orlando_Bloom_5', 'Orlando_Bloom_4', 'Orlando_Bloom_5', 'Orlando_Bloom_0', 'Ornella_Muti_2', 'Ornella_Muti_0', 'Orrin_Hatch_2', 'Orrin_Hatch_5', 'Oscar_DLeon_0', 'Oscar_DLeon_2', 'Oscar_Elias_Biscet_0', 'Oscar_Elias_Biscet_5', 'Otto_Reich_3', 'Otto_Reich_0', 'Otto_Reich_3', 'Otto_Reich_1', 'Otto_Schily_5', 'Otto_Schily_4', 'Laura_Bush_5', 'Nancy_Reagan_3', 'Krishna_Bhadur_Mahara_3', 'Louis_Van_Gaal_1', 'Leszek_Miller_3', 'Mahmoud_Abbas_1', 'Kenneth_Branagh_3', 'Martin_McGuinness_4', 'Kate_Winslet_0', 'Natasha_Henstridge_1', 'Nicanor_Duarte_Frutos_2', 'Otto_Reich_3', 'Laura_Elena_Harring_5', 'Mariana_Ohata_3', 'Kristin_Scott_4', 'Nina_Jacobson_1', 'Mario_Lobo_Zagallo_1', 'Otto_Schily_5', 'Marieta_Chrousala_1', 'Nina_Jacobson_3', 'Mariana_Ohata_0', 'Mary_Carey_0', 'Kathryn_Morris_2', 'Lesia_Burlak_3', 'Kathryn_Morris_2', 'Nina_Jacobson_3', 'Luis_Ernesto_Derbez_Bautista_1', 'Luiz_Inacio_Lula_da_Silva_4', 'Karin_Viard_1', 'Martha_Lucia_Ramirez_3', 'Lisa_Marie_Presley_1', 'Ornella_Muti_0', 'Matt_Anderson_2', 'Nuon_Chea_0', 'Katharine_Hepburn_1', 'Kristen_Breitweiser_5', 'Linda_Mason_5', 'Nora_Ephron_4', 'Lucio_Stanca_4', 'Nicanor_Duarte_Frutos_2', 'Lincoln_Chafee_3', 'Mary_Robinson_5', 'Linda_Dano_3', 'Nina_Jacobson_3', 'Maria_Soledad_Alvear_Valenzuela_4', 'Mary_Matalin_0', 'Linda_Dano_3', 'Maria_Bello_3', 'Kathryn_Morris_2', 'Natasa_Micic_5', 'Laura_Elena_Harring_5', 'Lyle_Lovett_2', 'Lino_Oviedo_3', 'Nicolas_Sarkozy_1', 'Liv_Tyler_3', 'Ornella_Muti_0', 'Nancy_Kerrigan_3', 'Ornella_Muti_0', 'Laura_Bush_5', 'Natasa_Micic_5', 'Lauren_Hutton_5', 'Manuel_Pellegrini_3', 'Kevin_Borseth_2', 'Kyle_Shewfelt_0', 'Luis_Fonsi_5', 'Norm_Macdonald_0', 'Lindsey_Graham_3', 'Lino_Oviedo_5', 'Katalin_Kollat_4', 'Noel_Niell_4', 'Larry_Brown_2', 'Orrin_Hatch_5', 'Nick_Reilly_4', 'Otto_Schily_4', 'Martin_Sheen_0', 'Nuon_Chea_0', 'Lincoln_Chafee_2', 'Marc_Anthony_5', 'Lucio_Stanca_4', 'Mario_Kreutzberger_2', 'Lesia_Burlak_3', 'Nina_Jacobson_3', 'Leland_Chapman_4', 'Louis_Van_Gaal_1', 'Kristin_Scott_4', 'Leticia_Dolera_4', 'Luis_Fonsi_5', 'Oscar_Elias_Biscet_5', 'Lyle_Lovett_2', 'Nina_Jacobson_3', 'Kate_Capshaw_2', 'Katja_Riemann_0', 'Kathryn_Morris_2', 'Kristin_Scott_4', 'Laura_Bush_5', 'Lyle_Lovett_2', 'Laura_Bozzo_4', 'Linda_Franklin_4', 'Laura_Flessel_2', 'Lisa_Leslie_5', 'Kate_Capshaw_2', 'Lene_Espersen_1', 'Martin_Landau_0', 'Narendra_Modi_4', 'Leuris_Pupo_2', 'Newt_Gingrich_3', 'Kevin_Spacey_3', 'Mahmoud_Abbas_5', 'Luis_Fonsi_2', 'Martin_Landau_0', 'Kim_Gandy_0', 'Nicanor_Duarte_Frutos_3', 'Kevin_Borseth_2', 'Krishna_Bhadur_Mahara_3', 'Nicanor_Duarte_Frutos_1', 'Oscar_Elias_Biscet_0', 'Krishna_Bhadur_Mahara_3', 'Mack_Brown_0', 'Kenneth_Branagh_5', 'Lubomir_Zaoralek_2', 'Laura_Bozzo_4', 'Lorraine_Bracco_0', 'Mary_Landrieu_3', 'Massoud_Barzani_4', 'Louis_Van_Gaal_1', 'Newt_Gingrich_1', 'Marissa_Jaret_Winokur_3', 'Natalie_Stewart_2', 'Leuris_Pupo_2', 'Lindsey_Graham_1', 'Martin_McGuinness_4', 'Martin_Sheen_0', 'Liu_Ye_5', 'Martin_Landau_2', 'Karin_Viard_1', 'Kim_Cattrall_0', 'Leticia_Dolera_4', 'Marissa_Jaret_Winokur_3', 'Marc_Anthony_5', 'Martin_Landau_0', 'Laura_Elena_Harring_4', 'Linda_Franklin_4', 'Kevin_Satterfield_0', 'Martin_Luther_King_III_0', 'Kenneth_Branagh_5', 'Mary_Robinson_1', 'Kyle_Shewfelt_4', 'Mary_Landrieu_3', 'Marc_Anthony_2', 'Orlando_Bloom_0', 'Mark_Dacey_0', 'Norm_Macdonald_2', 'Katharine_Hepburn_1', 'Marina_Silva_2', 'Mahathir_Mohamad_3', 'Oscar_DLeon_2', 'Matt_LeBlanc_3', 'Oscar_Elias_Biscet_5', 'Kristy_Curry_2', 'Mariana_Ohata_2', 'Kristin_Chenoweth_5', 'Laurie_Laychak_4', 'Mahmoud_Abbas_1', 'Marissa_Jaret_Winokur_0', 'Linda_Sanchez_4', 'Massoud_Barzani_4', 'Kristen_Breitweiser_0', 'Lene_Espersen_2', 'Linda_Lingle_4', 'Margaret_Thatcher_5', 'Kate_Capshaw_2', 'Lesia_Burlak_2', 'Keith_Olbermann_1', 'Larry_Nichols_1', 'Lindsey_Graham_3', 'Lyle_Lovett_2', 'Kirsten_Dunst_0', 'Ludivine_Sagnier_0', 'Lyle_Lovett_5', 'Marc_Anthony_5', 'Larry_Brown_1', 'Mahmoud_Abbas_1', 'Margaret_Thatcher_5', 'Mark_Foley_5', 'King_Abdullah_II_1', 'Mario_Gallegos_3', 'Kristy_Curry_0', 'Olympia_Dukakis_4', 'Laura_Bush_2', 'Nancy_Kerrigan_4', 'Kenneth_Carlsen_3', 'Matt_Anderson_0', 'Keith_Tyson_1', 'Kirk_Ferentz_2', 'Kostya_Tszyu_1', 'Oscar_DLeon_0', 'Lesia_Burlak_0', 'Marisa_Tomei_1', 'Leticia_Van_de_Putte_1', 'Mary_Landrieu_3', 'Kenneth_Carlsen_3', 'Lene_Espersen_1', 'Nancy_Reagan_3', 'Nick_Reilly_1', 'Katharine_Hepburn_1', 'Nick_Nolte_5', 'Natalie_Stewart_2', 'Norah_Jones_2', 'Katharine_Hepburn_4', 'Marissa_Jaret_Winokur_3', 'Luis_Fonsi_2', 'Martin_McGuinness_4', 'Kyle_Shewfelt_0', 'Mario_Lobo_Zagallo_1', 'Laura_Pausini_0', 'Loretta_Lynn_Harper_0', 'Kirk_Ferentz_2', 'Louis_Van_Gaal_1', 'Luis_Ernesto_Derbez_Bautista_1', 'Otto_Schily_5', 'Kenneth_Branagh_3', 'Martin_Landau_0', 'Mark_Foley_4', 'Nobuyuki_Idei_1', 'Oscar_DLeon_2', 'Otto_Reich_4', 'Krishna_Bhadur_Mahara_3', 'Massoud_Barzani_4', 'Kenneth_Carlsen_3', 'Margaret_Thatcher_3', 'Lene_Espersen_1', 'Nancy_Pelosi_0', 'Mack_Brown_5', 'Mark_Leno_2', 'Marina_Silva_2', 'Nona_Gaye_5', 'Martin_Sheen_4', 'Nicolas_Cage_1', 'Kit_Bond_3', 'Mario_Lobo_Zagallo_1', 'Linda_Mason_5', 'Natasha_Lyonne_4', 'Mary_Robinson_5', 'Massoud_Barzani_4', 'Kevin_Borseth_0', 'Lester_Holt_4', 'Mark_Cuban_3', 'Nicolas_Cage_1', 'Kieran_Culkin_0', 'Liu_Ye_5', 'Kevin_Satterfield_0', 'Leonid_Kuchma_2', 'Kevin_Satterfield_1', 'Krishna_Bhadur_Mahara_3', 'Lee_Byung-woong_5', 'Liu_Ye_2', 'Laurence_Fishburne_4', 'Lewis_Booth_2', 'Katalin_Kollat_4', 'Louisa_Baileche_0', 'Maria_Bello_4', 'Norah_Jones_4', 'Larry_Nichols_0', 'Marc_Bulger_1', 'Lucia_Kenny_Anthony_0', 'Mark_Foley_1', 'Mahathir_Mohamad_0', 'Manuel_Llorente_0', 'Nancy_Pelosi_4', 'Otto_Schily_5', 'Lester_Holt_3', 'Nuon_Chea_0', 'Mahathir_Mohamad_2', 'Mary_Robinson_5', 'Lubomir_Zaoralek_2', 'Noel_Niell_1', 'Kweisi_Mfume_5', 'Laurence_Fishburne_2', 'Larry_Brown_2', 'Mark_Geragos_2', 'Leszek_Miller_1', 'Nuon_Chea_0', 'Kim_Cattrall_0', 'Natalie_Cole_2', 'Kyle_Shewfelt_0', 'Lisa_Leslie_3', 'Kyle_Shewfelt_0', 'Laura_Elena_Harring_5', 'Louisa_Baileche_0', 'Mark_Cuban_3', 'Lindsey_Graham_1', 'Marieta_Chrousala_1', 'Kurt_Warner_0', 'Nanni_Moretti_1', 'Kirk_Ferentz_0', 'Newt_Gingrich_3', 'Matt_LeBlanc_3', 'Nancy_Reagan_3', 'King_Abdullah_II_4', 'Nancy_Reagan_3', 'Kevin_Satterfield_1', 'Orrin_Hatch_5', 'Nicolas_Eyzaguirre_0', 'Noel_Niell_1', 'Linda_Franklin_0', 'Olene_Walker_4', 'Leszek_Miller_1', 'Massoud_Barzani_4', 'Luiz_Inacio_Lula_da_Silva_4', 'Nathan_Lane_0', 'Mario_Lobo_Zagallo_1', 'Oscar_Elias_Biscet_0', 'Laura_Bozzo_4', 'Nadine_Vinzens_4', 'Maria_Soledad_Alvear_Valenzuela_1', 'Marina_Silva_2', 'Lena_Olin_1', 'Nona_Gaye_4', 'Kit_Bond_2', 'Otto_Reich_3', 'Matt_Anderson_2', 'Oscar_DLeon_2', 'Margaret_Thatcher_5', 'Maria_Callas_1', 'Kristen_Breitweiser_2', 'Nadia_Petrova_5', 'Keith_Tyson_2', 'Otto_Schily_4', 'Lewis_Booth_2', 'Mary_Robinson_5', 'Kristy_Curry_2', 'Laurence_Fishburne_2', 'Lesia_Burlak_3', 'Leticia_Dolera_4', 'Natalia_Verbeke_5', 'Ornella_Muti_0', 'Martin_Sheen_3', 'Natasha_Henstridge_1', 'Liu_Ye_5', 'Mack_Brown_5', 'Maria_Callas_1', 'Natasa_Micic_5', 'Marissa_Jaret_Winokur_0', 'Nicolas_Cage_0', 'Katja_Riemann_0', 'Nikki_McKibbin_5', 'Lewis_Booth_2', 'Natalie_Cole_5', 'Manuel_Pellegrini_3', 'Nanni_Moretti_4', 'Matt_LeBlanc_3', 'Nicolas_Cage_1', 'Marc_Anthony_5', 'Matt_LeBlanc_3', 'Lee_Baca_0', 'Martin_Landau_0', 'Natasha_McElhone_1', 'Nora_Ephron_4', 'Leuris_Pupo_4', 'Nursultan_Nazarbayev_3', 'Kate_Winslet_5', 'Louis_Van_Gaal_1', 'Luis_Ernesto_Derbez_Bautista_0', 'Massoud_Barzani_4', 'Laura_Linney_0', 'Liane_Janda_1', 'Kyle_Shewfelt_4', 'Mahmoud_Abbas_1', 'Kyle_Shewfelt_4', 'Natalia_Verbeke_3', 'Lino_Oviedo_0', 'Manuel_Llorente_0', 'Laura_Linney_4', 'Louisa_Baileche_1', 'Loretta_Lynn_Harper_0', 'Nikki_McKibbin_0', 'Mark_Foley_5', 'Oscar_Elias_Biscet_0', 'Keith_Olbermann_1', 'Kelsey_Grammer_4', 'Laura_Bozzo_1', 'Leticia_Dolera_4', 'Laurie_Laychak_0', 'Marissa_Jaret_Winokur_3', 'Kate_Winslet_0', 'Kieran_Culkin_2', 'Lucia_Kenny_Anthony_0', 'Nicolas_Sarkozy_5', 'Kelsey_Grammer_4', 'Nick_Rimando_3', 'Linda_Mason_4', 'Loretta_Lynn_Harper_5', 'Marc_Shaiman_3', 'Nicolas_Eyzaguirre_1', 'Marissa_Jaret_Winokur_0', 'Martin_Landau_0', 'Kristy_Curry_2', 'Lincoln_Chafee_5', 'Martin_McGuinness_4', 'Noel_Niell_1', 'Marc_Bulger_1', 'Mario_Cipollini_1', 'Leuris_Pupo_2', 'Nick_Nolte_2', 'Katalin_Kollat_4', 'Maria_Shriver_4', 'Leszek_Miller_3', 'Manuel_Pellegrini_1', 'Kristy_Curry_2', 'Lyle_Lovett_2', 'Keith_Olbermann_5', 'Kevin_Borseth_0', 'Natasa_Micic_0', 'Norah_Jones_4', 'Kenneth_Branagh_5', 'Laura_Elena_Harring_5', 'Laurence_Fishburne_4', 'Nicolas_Cage_0', 'Katharine_Hepburn_3', 'Louisa_Baileche_2', 'Kevin_Borseth_0', 'Lucia_Kenny_Anthony_0', 'Lyle_Lovett_2', 'Martin_Luther_King_III_0', 'Mario_Kreutzberger_3', 'Martin_Sheen_5', 'Kate_Capshaw_2', 'Noel_Niell_4', 'Matt_LeBlanc_3', 'Nadia_Petrova_4', 'Kate_Capshaw_1', 'Natasha_Henstridge_3', 'Laurence_Tribe_0', 'Orrin_Hatch_2', 'Katharine_Hepburn_1', 'Mark_Cuban_3', 'Larry_Brown_2', 'Nathan_Lane_0', 'Mark_Geragos_4', 'Olympia_Dukakis_1', 'Leticia_Dolera_4', 'Linda_Lingle_2', 'Larry_Wilmore_2', 'Mark_Dacey_3', 'Kevin_Borseth_0', 'Nancy_Reagan_3', 'Lena_Olin_0', 'Lisa_Leslie_5', 'Lino_Oviedo_3', 'Martin_Luther_King_III_3', 'Martin_McGuinness_4', 'Narendra_Modi_1', 'Lucia_Kenny_Anthony_0', 'Marina_Silva_4', 'Mario_Gallegos_3', 'Nick_Rimando_2', 'Lee_Baca_0', 'Nancy_Reagan_3', 'Larry_Flynt_0', 'Oscar_DLeon_2', 'Kirk_Ferentz_5', 'Orlando_Bloom_0', 'Kenneth_Reichert_2', 'Kristy_Curry_2', 'Maria_Callas_2', 'Noel_Niell_4', 'Oliver_Phelps_2', 'Orlando_Bloom_4', 'Kevin_Spacey_2', 'Mark_Kelly_0']

root_dirs = ["normalized_faces_mtcnn_cropped/" + root_dir for root_dir in root_dirs]

image_paths = get_image_paths(root_dirs)

features_dict = {}

for folder, filename, image_path in image_paths:
    image = Image.open(image_path)
    try:
        image_features = DeepFace.represent(img_path=image_path, model_name="Facenet512", enforce_detection=True,
                                            detector_backend="mtcnn")
    except ValueError as e:
        print(f"No face found in {filename}. Skipping.")
        continue

    if isinstance(image_features, list):
        image_features = np.array(image_features)

    features = np.concatenate([[folder, filename], image_features.flatten()])

    directory_name = os.path.basename(os.path.normpath(folder))

    if directory_name not in features_dict:
        features_dict[directory_name] = []
    features_dict[directory_name].append(features)

for directory_name, features in features_dict.items():
    features = np.array(features)

    csv_file = f"aaa/allFiles/{directory_name}_features.csv"
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Folder", "Filename", "Embedding"])
        writer.writerows(features)


# import os
# import numpy as np
# import csv
# from PIL import Image
# from deepface import DeepFace
#
#
# def get_image_paths(root_dir):
#     # Initialize an empty list to store image paths
#     image_paths = []
#
#     # Walk through the directory tree
#     for root, dirs, files in os.walk(root_dir):
#         # Loop through the files in the current directory
#         for file in files:
#             # Check if the file is an image file
#             if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
#                 # Construct the absolute path of the image file
#                 image_path = os.path.join(root, file)
#                 # Append the image path to the list along with folder and filename
#                 image_paths.append((root, file, image_path))
#
#     return image_paths
#
#
# root_dir = "normalized_faces_mtcnn_cropped/Mario_Lobo_Zagallo_1"
#
# image_paths = get_image_paths(root_dir)
#
# features = []
#
# for folder, filename, image_path in image_paths:
#     # Open the image using PIL (Python Imaging Library)
#     image = Image.open(image_path)
#
#     # Use DeepFace to detect and represent faces in the image
#     try:
#         # Extract features from the image using DeepFace library and VGG-Face model
#         image_features = DeepFace.represent(img_path=image_path, model_name="Facenet512", enforce_detection=True, detector_backend="mtcnn")
#     except ValueError as e:
#         # If no face is found, skip this image
#         print(f"No face found in {filename}. Skipping.")
#         continue
#
#     # Check if features is a list, convert it to a NumPy array if necessary
#     if isinstance(image_features, list):
#         image_features = np.array(image_features)
#
#     # Flatten the features into a 1D array
#     features.append(np.concatenate([[folder, filename], image_features.flatten()]))
#
# # Convert features to numpy array
# features = np.array(features)
#
# csv_file = "aaa/all/Mario_Lobo_Zagallo_1_features.csv"
# with open(csv_file, 'w', newline='') as file:
#     writer = csv.writer(file)
#     # Write the column names as the first row
#     writer.writerow(["Folder", "Filename", "Embedding"])
#     # Write the features to the CSV file
#     writer.writerows(features)
#
# # Luis_Fonsi_2.npz,Martin_Landau_0.npz