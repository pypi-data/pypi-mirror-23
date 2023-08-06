# -*- coding: utf-8 -*-

from __future__ import division

from openfisca_france.model.base import *  # noqa analysis:ignore

# Variables apparaissant dans la feuille de déclaration de patrimoine soumis à l'ISF

## Immeubles bâtis
class b1ab(Variable):
    column = IntCol(val_type = "monetary")
    entity = FoyerFiscal
    label = u"Valeur de la résidence principale avant abattement"
    definition_period = YEAR


class b1ac(Variable):
    column = IntCol(val_type = "monetary")
    entity = FoyerFiscal
    label = u"Valeur des autres immeubles avant abattement"
    definition_period = YEAR


## non bâtis
class b1bc(Variable):
    column = IntCol(val_type = "monetary")
    entity = FoyerFiscal
    label = u"Immeubles non bâtis : bois, fôrets et parts de groupements forestiers"
    definition_period = YEAR


class b1be(Variable):
    column = IntCol(val_type = "monetary")
    entity = FoyerFiscal
    label = u"Immeubles non bâtis : biens ruraux loués à long termes"
    definition_period = YEAR


class b1bh(Variable):
    column = IntCol(val_type = "monetary")
    entity = FoyerFiscal
    label = u"Immeubles non bâtis : parts de groupements fonciers agricoles et de groupements agricoles fonciers"
    definition_period = YEAR


class b1bk(Variable):
    column = IntCol(val_type = "monetary")
    entity = FoyerFiscal
    label = u"Immeubles non bâtis : autres biens"
    definition_period = YEAR


## droits sociaux- valeurs mobilières-liquidités- autres meubles
class b1cl(Variable):
    column = IntCol(val_type = "monetary")
    entity = FoyerFiscal
    label = u"Parts et actions détenues par les salariés et mandataires sociaux"
    definition_period = YEAR


class b1cb(Variable):
    column = IntCol(val_type = "monetary")
    entity = FoyerFiscal
    label = u"Parts et actions de sociétés avec engagement de conservation de 6 ans minimum"
    definition_period = YEAR


class b1cd(Variable):
    column = IntCol(val_type = "monetary")
    entity = FoyerFiscal
    label = u"Droits sociaux de sociétés dans lesquelles vous exercez une fonction ou une activité"
    definition_period = YEAR


class b1ce(Variable):
    column = IntCol(val_type = "monetary")
    entity = FoyerFiscal
    label = u"Autres valeurs mobilières"
    definition_period = YEAR


class b1cf(Variable):
    column = IntCol(val_type = "monetary")
    entity = FoyerFiscal
    label = u"Liquidités"
    definition_period = YEAR


class b1cg(Variable):
    column = IntCol(val_type = "monetary")
    entity = FoyerFiscal
    label = u"Autres biens meubles"
    definition_period = YEAR


class b1co(Variable):
    column = IntCol(val_type = "monetary")
    entity = FoyerFiscal
    label = u"Autres biens meubles : contrats d'assurance-vie"
    definition_period = YEAR


#    b1ch
#    b1ci
#    b1cj
#    b1ck


## passifs et autres réductions
class b2gh(Variable):
    column = IntCol(val_type = "monetary")
    entity = FoyerFiscal
    label = u"Total du passif et autres déductions"
    definition_period = YEAR


## réductions
class b2mt(Variable):
    column = IntCol(val_type = "monetary")
    entity = FoyerFiscal
    label = u"Réductions pour investissements directs dans une société"
    definition_period = YEAR


class b2ne(Variable):
    column = IntCol(val_type = "monetary")
    entity = FoyerFiscal
    label = u"Réductions pour investissements directs dans une société"
    definition_period = YEAR


class b2mv(Variable):
    column = IntCol(val_type = "monetary")
    entity = FoyerFiscal
    label = u"Réductions pour investissements par sociétés interposées, holdings"
    definition_period = YEAR


class b2nf(Variable):
    column = IntCol(val_type = "monetary")
    entity = FoyerFiscal
    label = u"Réductions pour investissements par sociétés interposées, holdings"
    definition_period = YEAR


class b2mx(Variable):
    column = IntCol(val_type = "monetary")
    entity = FoyerFiscal
    label = u"Réductions pour investissements par le biais de FIP"
    definition_period = YEAR


class b2na(Variable):
    column = IntCol(val_type = "monetary")
    entity = FoyerFiscal
    label = u"Réductions pour investissements par le biais de FCPI ou FCPR"
    definition_period = YEAR


class b2nc(Variable):
    column = IntCol(val_type = "monetary")
    entity = FoyerFiscal
    label = u"Réductions pour dons à certains organismes d'intérêt général"
    definition_period = YEAR


##  montant impôt acquitté hors de France
class b4rs(Variable):
    column = IntCol(val_type = "monetary")
    entity = FoyerFiscal
    label = u"Montant de l'impôt acquitté hors de France"
    definition_period = YEAR


## BOUCLIER FISCAL

class rev_or(Variable):
    column = IntCol(val_type = "monetary")
    entity = FoyerFiscal
    definition_period = YEAR


class rev_exo(Variable):
    column = IntCol(val_type = "monetary")
    entity = FoyerFiscal
    definition_period = YEAR


class tax_fonc(Variable):
    column = IntCol(val_type = "monetary")
    entity = FoyerFiscal
    label = u"Taxe foncière"
    definition_period = YEAR


class restit_imp(Variable):
    column = IntCol(val_type = "monetary")
    entity = FoyerFiscal
    definition_period = YEAR


class etr(Variable):
    column = IntCol
    entity = Individu
    definition_period = MONTH
    set_input = set_input_divide_by_period



# Calcul de l'impôt de solidarité sur la fortune

# 1 ACTIF BRUT

class isf_imm_bati(Variable):
    column = FloatCol(default = 0)
    entity = FoyerFiscal
    label = u"isf_imm_bati"
    definition_period = YEAR

    def formula(self, simulation, period):
        '''
        Immeubles bâtis
        '''
        b1ab = simulation.calculate('b1ab', period)
        b1ac = simulation.calculate('b1ac', period)
        P = simulation.legislation_at(period.start).taxation_capital.isf.res_princ

        return (1 - P.abattement_sur_residence_principale) * b1ab + b1ac


class isf_imm_non_bati(Variable):
    column = FloatCol(default = 0)
    entity = FoyerFiscal
    label = u"isf_imm_non_bati"
    definition_period = YEAR

    def formula(self, simulation, period):
        '''
        Immeubles non bâtis
        '''
        b1bc = simulation.calculate('b1bc', period)
        b1be = simulation.calculate('b1be', period)
        b1bh = simulation.calculate('b1bh', period)
        b1bk = simulation.calculate('b1bk', period)
        P = simulation.legislation_at(period.start).taxation_capital.isf.nonbat

        # forêts
        b1bd = b1bc * P.taux_f
        # bien ruraux loués à long terme
        b1bf = min_(b1be, P.seuil) * P.taux_r1
        b1bg = max_(b1be - P.seuil, 0) * P.taux_r2
        # part de groupements forestiers- agricoles fonciers
        b1bi = min_(b1bh, P.seuil) * P.taux_r1
        b1bj = max_(b1bh - P.seuil, 0) * P.taux_r2
        return b1bd + b1bf + b1bg + b1bi + b1bj + b1bk


# # droits sociaux- valeurs mobilières- liquidités- autres meubles ##


class isf_actions_sal(Variable):  # # non présent en 2005##
    column = FloatCol(default = 0)
    entity = FoyerFiscal
    label = u"isf_actions_sal"
    definition_period = YEAR

    def formula_2006(self, simulation, period):
        '''
        Parts ou actions détenues par les salariés et mandataires sociaux
        '''
        b1cl = simulation.calculate('b1cl', period)
        P = simulation.legislation_at(period.start).taxation_capital.isf.droits_soc

        return  b1cl * P.taux1


class isf_droits_sociaux(Variable):
    column = FloatCol(default = 0)
    entity = FoyerFiscal
    label = u"isf_droits_sociaux"
    definition_period = YEAR

    def formula(self, simulation, period):
        isf_actions_sal = simulation.calculate('isf_actions_sal', period)
        b1cb = simulation.calculate('b1cb', period)
        b1cd = simulation.calculate('b1cd', period)
        b1ce = simulation.calculate('b1ce', period)
        b1cf = simulation.calculate('b1cf', period)
        b1cg = simulation.calculate('b1cg', period)
        P = simulation.legislation_at(period.start).taxation_capital.isf.droits_soc

        b1cc = b1cb * P.taux2
        return isf_actions_sal + b1cc + b1cd + b1ce + b1cf + b1cg


class ass_isf(Variable):
    column = FloatCol(default = 0)
    entity = FoyerFiscal
    label = u"ass_isf"
    definition_period = YEAR

    def formula(self, simulation, period):
        # TODO: Gérer les trois option meubles meublants
        isf_imm_bati = simulation.calculate('isf_imm_bati', period)
        isf_imm_non_bati = simulation.calculate('isf_imm_non_bati', period)
        isf_droits_sociaux = simulation.calculate('isf_droits_sociaux', period)
        b1cg = simulation.calculate('b1cg', period)
        b2gh = simulation.calculate('b2gh', period)
        P = simulation.legislation_at(period.start).taxation_capital.isf.forf_mob

        total = isf_imm_bati + isf_imm_non_bati + isf_droits_sociaux
        forf_mob = (b1cg != 0) * b1cg + (b1cg == 0) * total * P.taux
        actif_brut = total + forf_mob
        return actif_brut - b2gh


# # calcul de l'impôt par application du barème ##


class isf_iai(Variable):
    column = FloatCol(default = 0)
    entity = FoyerFiscal
    label = u"isf_iai"
    definition_period = YEAR

    def formula_2002_01_01(self, simulation, period):
        ass_isf = simulation.calculate('ass_isf', period)
        bareme = simulation.legislation_at(period.start).taxation_capital.isf.bareme
        return bareme.calc(ass_isf)

    # Cette formule a seulement été vérifiée jusqu'au 2015-12-31
    def formula_2011_01_01(self, simulation, period):
        ass_isf = simulation.calculate('ass_isf', period)
        bareme = simulation.legislation_at(period.start).taxation_capital.isf.bareme
        ass_isf = (ass_isf >= bareme.rates[1]) * ass_isf
        return bareme.calc(ass_isf)


class isf_avant_reduction(Variable):
    column = FloatCol(default = 0)
    entity = FoyerFiscal
    label = u"isf_avant_reduction"
    definition_period = YEAR

    def formula(self, simulation, period):
        isf_iai = simulation.calculate('isf_iai', period)
        decote_isf = simulation.calculate('decote_isf', period)

        return isf_iai - decote_isf


class isf_reduc_pac(Variable):
    column = FloatCol(default = 0)
    entity = FoyerFiscal
    label = u"isf_reduc_pac"
    end = '2012-12-31'
    definition_period = YEAR

    def formula(self, simulation, period):
        '''
        Réductions pour personnes à charges
        '''
        nb_pac = simulation.calculate('nb_pac', period)
        nbH = simulation.calculate('nbH', period)
        P = simulation.legislation_at(period.start).taxation_capital.isf.reduc_pac

        return P.reduc_enf_garde * nb_pac + (P.reduc_enf_garde / 2) * nbH



class isf_inv_pme(Variable):
    column = FloatCol(default = 0)
    entity = FoyerFiscal
    label = u"isf_inv_pme"
    definition_period = YEAR

    def formula_2008(self, simulation, period):
        '''
        Réductions pour investissements dans les PME
        à partir de 2008!
        '''
        b2mt = simulation.calculate('b2mt', period)
        b2ne = simulation.calculate('b2ne', period)
        b2mv = simulation.calculate('b2mv', period)
        b2nf = simulation.calculate('b2nf', period)
        b2mx = simulation.calculate('b2mx', period)
        b2na = simulation.calculate('b2na', period)
        P = simulation.legislation_at(period.start).taxation_capital.isf.reduc_invest_don

        inv_dir_soc = b2mt * P.taux_don_interet_general + b2ne * P.taux_invest_direct_soc_holding
        holdings = b2mv * P.taux_don_interet_general + b2nf * P.taux_invest_direct_soc_holding
        fip = b2mx * P.taux_invest_direct_soc_holding
        fcpi = b2na * P.taux_invest_direct_soc_holding


        return holdings + fip + fcpi + inv_dir_soc


class isf_org_int_gen(Variable):
    column = FloatCol(default = 0)
    entity = FoyerFiscal
    label = u"isf_org_int_gen"
    definition_period = YEAR

    def formula_2008(self, simulation, period):
        b2nc = simulation.calculate('b2nc', period)
        P = simulation.legislation_at(period.start).taxation_capital.isf.reduc_invest_don

        return b2nc * P.taux_don_interet_general

class isf_avant_plaf(Variable):
    column = FloatCol(default = 0)
    entity = FoyerFiscal
    label = u"Montant de l'impôt sur la fortune avant plafonnement"
    definition_period = YEAR

    def formula(self, simulation, period):
        isf_avant_reduction = simulation.calculate('isf_avant_reduction', period)
        isf_reduc_pac = simulation.calculate('isf_reduc_pac', period)

        return max_(0, isf_avant_reduction - isf_reduc_pac)

    def formula_2008(self, simulation, period):
        isf_avant_reduction = simulation.calculate('isf_avant_reduction', period)
        isf_inv_pme = simulation.calculate('isf_inv_pme', period)
        isf_org_int_gen = simulation.calculate('isf_org_int_gen', period)
        isf_reduc_pac = simulation.calculate('isf_reduc_pac', period)

        return max_(0, isf_avant_reduction - (isf_inv_pme + isf_org_int_gen) - isf_reduc_pac)

    def formula_2009(self, simulation, period):
        isf_avant_reduction = simulation.calculate('isf_avant_reduction', period)
        isf_inv_pme = simulation.calculate('isf_inv_pme', period)
        isf_org_int_gen = simulation.calculate('isf_org_int_gen', period)
        isf_reduc_pac = simulation.calculate('isf_reduc_pac', period)
        borne_max = simulation.legislation_at(period.start).taxation_capital.isf.reduc_invest_don.max

        return max_(0, isf_avant_reduction - min_(isf_inv_pme + isf_org_int_gen, borne_max) - isf_reduc_pac)


# # calcul du plafonnement ##
class tot_impot(Variable):
    column = FloatCol(default = 0)
    entity = FoyerFiscal
    label = u"tot_impot"
    definition_period = YEAR

    def formula(self, simulation, period):
        '''
        Total des impôts dus au titre des revenus et produits (irpp, cehr, pl, prélèvements sociaux) + ISF
        Utilisé pour calculer le montant du plafonnement de l'ISF
        '''
        irpp = simulation.calculate('irpp', period)
        isf_avant_plaf = simulation.calculate('isf_avant_plaf', period)
        crds_holder = simulation.compute('crds', period)
        csg_holder = simulation.compute('csg', period)
        prelsoc_cap_holder = simulation.compute('prelsoc_cap', period)

        crds = self.split_by_roles(crds_holder, roles = [VOUS, CONJ])
        csg = self.split_by_roles(csg_holder, roles = [VOUS, CONJ])
        prelsoc_cap = self.split_by_roles(prelsoc_cap_holder, roles = [VOUS, CONJ])

        return (-irpp + isf_avant_plaf -
            (crds[VOUS] + crds[CONJ]) - (csg[VOUS] + csg[CONJ]) - (prelsoc_cap[VOUS] + prelsoc_cap[CONJ])
            )

        # TODO: irpp n'est pas suffisant : ajouter ir soumis à taux propor + impôt acquitté à l'étranger
        # + prélèvement libé de l'année passée + montant de la csg


class revetproduits(Variable):
    column = FloatCol(default = 0)
    entity = FoyerFiscal
    label = u"Revenus et produits perçus (avant abattement)"
    definition_period = YEAR

    def formula(self, simulation, period):
        '''
        Utilisé pour calculer le montant du plafonnement de l'ISF
        Cf.
        http://www.impots.gouv.fr/portal/deploiement/p1/fichedescriptiveformulaire_8342/fichedescriptiveformulaire_8342.pdf
        '''
        salcho_imp_holder = simulation.compute('revenu_assimile_salaire_apres_abattements', period)
        pen_net_holder = simulation.compute('revenu_assimile_pension_apres_abattements', period)
        retraite_titre_onereux_net = simulation.calculate('retraite_titre_onereux_net', period)
        rev_cap_bar = simulation.calculate_add('rev_cap_bar', period)
        fon = simulation.calculate('fon', period)
        ric_holder = simulation.compute('ric', period)
        rag_holder = simulation.compute('rag', period)
        rpns_exon_holder = simulation.compute('rpns_exon', period)
        rpns_pvct_holder = simulation.compute('rpns_pvct', period)
        rev_cap_lib = simulation.calculate_add('rev_cap_lib', period)
        imp_lib = simulation.calculate('imp_lib', period)
        P = simulation.legislation_at(period.start).taxation_capital.isf.plafonnement

        revenu_assimile_pension_apres_abattements = self.sum_by_entity(pen_net_holder)
        rag = self.sum_by_entity(rag_holder)
        ric = self.sum_by_entity(ric_holder)
        rpns_exon = self.sum_by_entity(rpns_exon_holder)
        rpns_pvct = self.sum_by_entity(rpns_pvct_holder)
        revenu_assimile_salaire_apres_abattements = self.sum_by_entity(salcho_imp_holder)

        # rev_cap et imp_lib pour produits soumis à prel libératoire- check TODO:
        # # def rev_exon et rev_etranger dans data? ##
        pt = max_(
            0,
            revenu_assimile_salaire_apres_abattements + revenu_assimile_pension_apres_abattements + retraite_titre_onereux_net + rev_cap_bar + rev_cap_lib + ric + rag + rpns_exon +
            rpns_pvct + imp_lib + fon
            )
        return pt * P.plafonnement_taux_d_imposition_isf


class decote_isf(Variable):
    column = FloatCol(default = 0)
    entity = FoyerFiscal
    label = u"Décote de l'ISF"
    definition_period = YEAR

    def formula_2013(self, simulation, period):
        ass_isf = simulation.calculate('ass_isf', period)
        P = simulation.legislation_at(period.start).taxation_capital.isf.decote

        elig = (ass_isf >= P.isf_borne_min_decote) & (ass_isf <= P.isf_borne_sup_decote)
        LB = P.isf_base_decote - P.isf_taux_decote * ass_isf
        return LB * elig


class isf_apres_plaf(Variable):
    column = FloatCol(default = 0)
    entity = FoyerFiscal
    label = u"Impôt sur la fortune après plafonnement"
    definition_period = YEAR
    # Plafonnement supprimé pour l'année 2012

    def formula_2002_01_01(self, simulation, period):
        tot_impot = simulation.calculate('tot_impot', period)
        revetproduits = simulation.calculate('revetproduits', period)
        isf_avant_plaf = simulation.calculate('isf_avant_plaf', period)
        P = simulation.legislation_at(period.start).taxation_capital.isf.plaf

        # si ISF avant plafonnement n'excède pas seuil 1= la limitation du plafonnement ne joue pas
        # si entre les deux seuils; l'allègement est limité au 1er seuil
        # si ISF avant plafonnement est supérieur au 2nd seuil, l'allègement qui résulte du plafonnement
        #    est limité à 50% de l'ISF
        plafonnement = max_(tot_impot - revetproduits, 0)
        limitationplaf = (
            (isf_avant_plaf <= P.seuil1) * plafonnement +
            (P.seuil1 <= isf_avant_plaf) * (isf_avant_plaf <= P.seuil2) * min_(plafonnement, P.seuil1) +
            (isf_avant_plaf >= P.seuil2) * min_(isf_avant_plaf * P.taux, plafonnement)
            )
        return max_(isf_avant_plaf - limitationplaf, 0)

    def formula_2012_01_01(self, simulation, period):
        isf_avant_plaf = simulation.calculate('isf_avant_plaf', period)

        # si ISF avant plafonnement n'excède pas seuil 1= la limitation du plafonnement ne joue pas ##
        # si entre les deux seuils; l'allègement est limité au 1er seuil ##
        # si ISF avant plafonnement est supérieur au 2nd seuil, l'allègement qui résulte du plafonnement
        #    est limité à 50% de l'ISF
        return isf_avant_plaf

    # Cette formule a seulement été vérifiée jusqu'au 2015-12-31
    def formula_2013_01_01(self, simulation, period):
        """
        Impôt sur la fortune après plafonnement
        """
        tot_impot = simulation.calculate('tot_impot', period)
        revetproduits = simulation.calculate('revetproduits', period)
        isf_avant_plaf = simulation.calculate('isf_avant_plaf', period)

        plafond = max_(0, tot_impot - revetproduits)  # case PU sur la déclaration d'impôt
        return max_(isf_avant_plaf - plafond, 0)


class isf_tot(Variable):
    column = FloatCol(default = 0)
    entity = FoyerFiscal
    label = u"isf_tot"
    reference = "http://www.impots.gouv.fr/portal/dgi/public/particuliers.impot?pageId=part_isf&espId=1&impot=ISF&sfid=50"
    definition_period = YEAR

    def formula(self, simulation, period):
        b4rs = simulation.calculate('b4rs', period)
        isf_avant_plaf = simulation.calculate('isf_avant_plaf', period)
        isf_apres_plaf = simulation.calculate('isf_apres_plaf', period)
        irpp = simulation.calculate('irpp', period)

        return min_(-((isf_apres_plaf - b4rs) * ((-irpp) > 0) + (isf_avant_plaf - b4rs) * ((-irpp) <= 0)), 0)


# # BOUCLIER FISCAL ##

# # calcul de l'ensemble des revenus du contribuable ##


# TODO: à reintégrer dans irpp
class rvcm_plus_abat(Variable):
    column = FloatCol(default = 0)
    entity = FoyerFiscal
    label = u"rvcm_plus_abat"
    definition_period = YEAR

    def formula(self, simulation, period):
        '''
        Revenu catégoriel avec abattement de 40% réintégré.
        '''
        rev_cat_rvcm = simulation.calculate('rev_cat_rvcm', period)
        rfr_rvcm = simulation.calculate('rfr_rvcm', period)

        return rev_cat_rvcm + rfr_rvcm


class maj_cga(Variable):
    column = FloatCol
    entity = Individu
    label = u"Majoration pour non adhésion à un centre de gestion agréé (pour chaque individu du foyer)"
    definition_period = YEAR

    # TODO: à reintégrer dans irpp (et vérifier au passage que frag_impo est dans la majo_cga
    def formula(self, simulation, period):
        frag_impo = simulation.calculate('frag_impo', period)
        nrag_impg = simulation.calculate('nrag_impg', period)
        nbic_impn = simulation.calculate('nbic_impn', period)
        nbic_imps = simulation.calculate('nbic_imps', period)
        nbic_defn = simulation.calculate('nbic_defn', period)
        nbic_defs = simulation.calculate('nbic_defs', period)
        nacc_impn = simulation.calculate('nacc_impn', period)
        nacc_meup = simulation.calculate('nacc_meup', period)
        nacc_defn = simulation.calculate('nacc_defn', period)
        nacc_defs = simulation.calculate('nacc_defs', period)
        nbnc_impo = simulation.calculate('nbnc_impo', period)
        nbnc_defi = simulation.calculate('nbnc_defi', period)
        P = simulation.legislation_at(period.start).impot_revenu.rpns

        nbic_timp = (nbic_impn + nbic_imps) - (nbic_defn + nbic_defs)

        # C revenus industriels et commerciaux non professionnels
        # (revenus accesoires du foyers en nomenclature INSEE)
        nacc_timp = max_(0, (nacc_impn + nacc_meup) - (nacc_defn + nacc_defs))

        # régime de la déclaration contrôlée ne bénéficiant pas de l'abattement association agréée
        nbnc_timp = nbnc_impo - nbnc_defi

        # Totaux
        ntimp = nrag_impg + nbic_timp + nacc_timp + nbnc_timp

        return max_(0, P.cga_taux2 * (ntimp + frag_impo))


class bouclier_rev(Variable):
    column = FloatCol(default = 0)
    entity = FoyerFiscal
    label = u"bouclier_rev"
    end = '2010-12-31'
    definition_period = YEAR

    def formula_2006(self, simulation, period):
        '''
        Total des revenus sur l'année 'n' net de charges
        '''
        rbg = simulation.calculate('rbg', period)
        csg_deduc = simulation.calculate('csg_deduc', period)
        rvcm_plus_abat = simulation.calculate('rvcm_plus_abat', period)
        rev_cap_lib = simulation.calculate('rev_cap_lib', period)
        rev_exo = simulation.calculate('rev_exo', period)
        rev_or = simulation.calculate('rev_or', period)
        pensions_alimentaires_deduites = simulation.calculate('pensions_alimentaires_deduites', period)
        cd_eparet = simulation.calculate('cd_eparet', period)

        maj_cga = simulation.calculate('maj_cga', period)
        maj_cga = simulation.foyer_fiscal.sum(maj_cga)

        # TODO: réintégrer les déficits antérieur
        # TODO: intégrer les revenus soumis au prélèvement libératoire
        # deficit_ante =

        # # Revenus
        frac_rvcm_rfr = 0.7 * rvcm_plus_abat  # TODO: UNUSED ?
        # # revenus distribués?
        # # A majorer de l'abatt de 40% - montant brut en cas de PFL
        # # pour le calcul de droit à restitution : prendre 0.7*montant_brut_rev_dist_soumis_au_barème
        # rev_bar = rbg - maj_cga - csg_deduc - deficit_ante
        rev_bar = rbg - maj_cga - csg_deduc

    # # TODO: AJOUTER : indemnités de fonction percus par les élus- revenus soumis à régimes spéciaux

        # Revenu soumis à l'impôt sur le revenu forfaitaire
        rev_lib = rev_cap_lib
        # # AJOUTER plus-values immo et moins values?

        # #Revenus exonérés d'IR réalisés en France et à l'étranger##
    #    rev_exo = primes_pel + primes_cel + rente_pea + int_livrets + plus_values_per

        # # proposer à l'utilisateur des taux de réference- PER, PEA, PEL,...TODO
        # # sommes investis- calculer les plus_values annuelles et prendre en compte pour rev_exo?
        # revenus soumis à la taxe forfaitaire sur les métaux précieux : rev_or

        # revenus = rev_bar + rev_lib + rev_exo + rev_or
        revenus = rev_bar + rev_lib + rev_or

        # # CHARGES
        # Pension alimentaires
        # Cotisations ou primes versées au titre de l'épargne retraite

        charges = pensions_alimentaires_deduites + cd_eparet

        return revenus - charges


class bouclier_imp_gen(Variable):  # # ajouter CSG- CRDS
    column = FloatCol(default = 0)
    entity = FoyerFiscal
    label = u"bouclier_imp_gen"
    end = '2010-12-31'
    definition_period = YEAR

    def formula_2006(self, simulation, period):
        irpp = simulation.calculate('irpp', period)
        taxe_habitation_holder = simulation.compute('taxe_habitation', period)
        tax_fonc = simulation.calculate('tax_fonc', period)
        isf_tot = simulation.calculate('isf_tot', period)
        csg_deductible_salaire_holder = simulation.compute('csg_deductible_salaire', period)
        csg_imposable_salaire_holder = simulation.compute('csg_imposable_salaire', period)
        crds_salaire_holder = simulation.compute('crds_salaire', period)
        csg_imposable_chomage_holder = simulation.compute('csg_imposable_chomage', period)
        csg_deductible_chomage_holder = simulation.compute('csg_deductible_chomage', period)
        csg_deductible_retraite_holder = simulation.compute('csg_deductible_retraite', period)
        csg_imposable_retraite_holder = simulation.compute('csg_imposable_retraite', period)
        imp_lib = simulation.calculate('imp_lib', period)

        cotsoc_bar = simulation.calculate('cotsoc_bar', period)
        cotsoc_lib = simulation.calculate('cotsoc_lib', period)
        crds_salaire = self.sum_by_entity(crds_salaire_holder)
        csg_deductible_chomage = self.sum_by_entity(csg_deductible_chomage_holder)
        csg_imposable_chomage = self.sum_by_entity(csg_imposable_chomage_holder)
        csg_deductible_salaire = self.sum_by_entity(csg_deductible_salaire_holder)
        csg_imposable_salaire = self.sum_by_entity(csg_imposable_salaire_holder)
        csg_deductible_retraite = self.sum_by_entity(csg_deductible_retraite_holder)
        csg_imposable_retraite = self.sum_by_entity(csg_imposable_retraite_holder)
        taxe_habitation = self.cast_from_entity_to_role(taxe_habitation_holder, role = PREF)
        taxe_habitation = self.sum_by_entity(taxe_habitation)

        # # ajouter Prelèvements sources/ libé
        # # ajouter crds rstd
        # # impôt sur les plus-values immo et cession de fonds de commerce
        imp1 = cotsoc_lib + cotsoc_bar + csg_deductible_salaire + csg_deductible_chomage + crds_salaire + csg_deductible_retraite + imp_lib
        '''
        Impôts payés en l'année 'n' au titre des revenus réalisés sur l'année 'n'
        '''
        imp2 = irpp + isf_tot + taxe_habitation + tax_fonc + csg_imposable_salaire + csg_imposable_chomage + csg_imposable_retraite
        '''
        Impôts payés en l'année 'n' au titre des revenus réalisés en 'n-1'
        '''
        return imp1 + imp2


class restitutions(Variable):
    column = FloatCol(default = 0)
    entity = FoyerFiscal
    label = u"restitutions"
    end = '2010-12-31'
    definition_period = YEAR

    def formula_2006(self, simulation, period):
        '''
        Restitutions d'impôt sur le revenu et degrèvements percus en l'année 'n'
        '''
        ppe = simulation.calculate('ppe', period)
        restit_imp = simulation.calculate('restit_imp', period)

        return ppe + restit_imp


class bouclier_sumimp(Variable):
    column = FloatCol(default = 0)
    entity = FoyerFiscal
    label = u"bouclier_sumimp"
    end = '2010-12-31'
    definition_period = YEAR

    def formula_2006(self, simulation, period):
        '''
        Somme totale des impôts moins restitutions et degrèvements
        '''
        bouclier_imp_gen = simulation.calculate('bouclier_imp_gen', period)
        restitutions = simulation.calculate('restitutions', period)

        return -bouclier_imp_gen + restitutions


class bouclier_fiscal(Variable):
    column = FloatCol(default = 0)
    entity = FoyerFiscal
    label = u"bouclier_fiscal"
    end = '2010-12-31'
    reference = "http://fr.wikipedia.org/wiki/Bouclier_fiscal"
    definition_period = YEAR

    def formula_2006(self, simulation, period):
        bouclier_sumimp = simulation.calculate('bouclier_sumimp', period)
        bouclier_rev = simulation.calculate('bouclier_rev', period)
        P = simulation.legislation_at(period.start).bouclier_fiscal

        return max_(0, bouclier_sumimp - (bouclier_rev * P.taux))
