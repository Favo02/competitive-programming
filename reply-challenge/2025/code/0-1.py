import sys
import math

class Resource:
    def __init__(self, resource_tuple):
        # resource_tuple: (RI, RA, RP, RW, RM, RL, RU, RT, RE)
        self.RI = resource_tuple[0]
        self.RA = resource_tuple[1]
        self.RP = resource_tuple[2]
        self.RW = resource_tuple[3]
        self.RM = resource_tuple[4]
        self.RL = resource_tuple[5]
        self.RU = resource_tuple[6]
        self.RT = resource_tuple[7]
        self.RE = resource_tuple[8] if len(resource_tuple) > 8 else None
        self.active = True
        self.active_phase = True
        self.cycles = 0
        self.current_turn_in_phase = 0
        # Per le risorse di tipo E gestiamo la carica accumulata
        if self.RT == 'E':
            self.accumulated = 0

    def advance_turn(self):
        if not self.active:
            return False
        self.current_turn_in_phase += 1
        if self.active_phase:
            if self.current_turn_in_phase >= self.RW:
                self.active_phase = False
                self.current_turn_in_phase = 0
                self.cycles += 1
        else:
            if self.current_turn_in_phase >= self.RM:
                self.active_phase = True
                self.current_turn_in_phase = 0

        total_turns = self.cycles * (self.RW + self.RM) + self.current_turn_in_phase
        if total_turns >= self.RL:
            self.active = False
        return self.active

def compute_active_turns(rw, rm, rl, current_turn, T):
    # Calcola quanti turni attivi la risorsa potrà dare se acquistata ora,
    # limitando la vita residua al tempo rimasto nel gioco (T - current_turn)
    turns_remaining = min(T - current_turn, rl)
    cycle = rw + rm
    full_cycles = turns_remaining // cycle
    remainder = turns_remaining % cycle
    active_turns = full_cycles * rw + min(rw, remainder)
    return active_turns

def main():
    input_lines = [line.strip() for line in sys.stdin.read().split('\n') if line.strip()]
    ptr = 0
    # Lettura parametri iniziali
    D, R, T = map(int, input_lines[ptr].split())
    ptr += 1

    # Lettura risorse: ogni riga è (RI, RA, RP, RW, RM, RL, RU, RT, [RE])
    res = []
    for _ in range(R):
        parts = input_lines[ptr].split()
        r_int = list(map(int, parts[:7]))
        rt = parts[7]
        re_val = int(parts[8]) if len(parts) > 8 and rt != 'X' else None
        res.append(tuple(r_int + [rt, re_val]))
        ptr += 1

    # Lettura dei turni: (TM, TX, TR)
    turns = []
    for _ in range(T):
        tm, tx, tr = map(int, input_lines[ptr].split())
        turns.append((tm, tx, tr))
        ptr += 1

    active_resources = []
    output = []
    budget = D

    for turn_num in range(T):
        tm_base, tx_base, tr_base = turns[turn_num]

        # Calcolo dell'effetto A corrente (smart meter) dalle risorse attive
        a_effect = 0.0
        for r in active_resources:
            if r.RT == 'A' and r.active_phase and r.active and r.RE is not None:
                a_effect += (r.RE / 100.0) if r.RE >= 0 else - (abs(r.RE) / 100.0)
        
        # Calcolo della capacità attuale (numero di edifici alimentati) al turno corrente
        current_power = 0
        for r in active_resources:
            if r.active and r.active_phase:
                effective_RU = max(0, math.floor(r.RU * (1 + a_effect)))
                current_power += effective_RU

        purchased_ids = []
        activation_cost_this_turn = 0

        # Fase di acquisto
        # Se la capacità attuale non raggiunge il minimo TM, cerchiamo di colmare il gap
        gap = tm_base - current_power
        if gap > 0:
            # Consideriamo solo risorse che aumentano direttamente la potenza: tipo A e X.
            candidate_pool = []
            for r in res:
                if r[7] in ['A', 'X']:
                    # Calcolo del contributo immediato: la risorsa è attiva già nello stesso turno
                    ru = r[6]
                    bonus = 0.0
                    if r[7] == 'A' and r[8] is not None and r[8] > 0:
                        bonus = r[8] / 100.0
                    immediate = ru * (1 + bonus)
                    ratio = immediate / r[1] if r[1] > 0 else immediate
                    candidate_pool.append((ratio, r))
            candidate_pool.sort(key=lambda x: x[0], reverse=True)
            # Acquisto ripetuto finché il gap non è colmato o il budget si esaurisce (attenzione al limite di 50 acquisti per turno)
            while gap > 0 and budget > 0 and len(purchased_ids) < 50:
                bought = False
                for ratio, candidate in candidate_pool:
                    if candidate[1] <= budget:
                        # Acquisto della risorsa candidate
                        purchased_ids.append(candidate[0])
                        activation_cost_this_turn += candidate[1]
                        budget -= candidate[1]
                        # Se sono presenti risorse di tipo C attive, modifico RL della nuova risorsa
                        c_effect = 0.0
                        for ar in active_resources:
                            if ar.RT == 'C' and ar.active_phase and ar.active and ar.RE is not None:
                                c_effect += (ar.RE / 100.0) if ar.RE >= 0 else - (abs(ar.RE) / 100.0)
                        new_rl = candidate[5]
                        if c_effect != 0:
                            new_rl = max(1, math.floor(candidate[5] * (1 + c_effect)))
                        new_resource = Resource((candidate[0], candidate[1], candidate[2],
                                                 candidate[3], candidate[4], new_rl,
                                                 candidate[6], candidate[7], candidate[8]))
                        active_resources.append(new_resource)
                        # Aggiorno il gap sottraendo il contributo immediato
                        effective_power = candidate[6]
                        if candidate[7] == 'A' and candidate[8] is not None and candidate[8] > 0:
                            effective_power = math.floor(candidate[6] * (1 + candidate[8] / 100.0))
                        gap -= effective_power
                        bought = True
                        break
                if not bought:
                    # Nessuna risorsa rientra nel budget
                    break

        # Se il gap è già coperto e c'è ancora budget, valutiamo investimenti a lungo termine
        if gap <= 0 and budget > 0 and len(purchased_ids) < 50:
            candidate_pool = []
            for r in res:
                if r[1] <= budget:
                    active_turns = compute_active_turns(r[3], r[4], r[5], turn_num, T)
                    total_power = r[6] * active_turns
                    # Aggiustiamo per eventuali effetti positivi di tipi A, D o B
                    multiplier = 1.0
                    if r[7] in ['A', 'D', 'B'] and r[8] is not None and r[8] > 0:
                        multiplier = 1 + r[8] / 100.0
                    total_power *= multiplier
                    efficiency = total_power / r[1] if r[1] > 0 else total_power
                    candidate_pool.append((efficiency, r))
            candidate_pool.sort(key=lambda x: x[0], reverse=True)
            for eff, candidate in candidate_pool:
                if budget <= 0 or len(purchased_ids) >= 50:
                    break
                if candidate[1] <= budget:
                    purchased_ids.append(candidate[0])
                    activation_cost_this_turn += candidate[1]
                    budget -= candidate[1]
                    c_effect = 0.0
                    for ar in active_resources:
                        if ar.RT == 'C' and ar.active_phase and ar.active and ar.RE is not None:
                            c_effect += (ar.RE / 100.0) if ar.RE >= 0 else - (abs(ar.RE) / 100.0)
                    new_rl = candidate[5]
                    if c_effect != 0:
                        new_rl = max(1, math.floor(candidate[5] * (1 + c_effect)))
                    new_resource = Resource((candidate[0], candidate[1], candidate[2],
                                             candidate[3], candidate[4], new_rl,
                                             candidate[6], candidate[7], candidate[8]))
                    active_resources.append(new_resource)
                    break  # Acquistiamo al massimo una risorsa "long-term" in più

        if purchased_ids:
            output.append(f"{turn_num} {len(purchased_ids)} " + " ".join(map(str, purchased_ids)))

        # STEP 2: Pagamento dei costi periodici (RP)
        maintenance_cost = sum(r.RP for r in active_resources if r.active)
        budget -= maintenance_cost

        # STEP 3: Calcolo degli effetti cumulativi
        # Effetto B: modifica di TM e TX
        b_effect = 0.0
        for r in active_resources:
            if r.RT == 'B' and r.active_phase and r.active and r.RE is not None:
                b_effect += (r.RE / 100.0)
        effective_tm = max(0, math.floor(tm_base * (1 + b_effect)))
        effective_tx = max(0, math.floor(tx_base * (1 + b_effect)))
        # Effetto D: modifica di TR
        d_effect = 0.0
        for r in active_resources:
            if r.RT == 'D' and r.active_phase and r.active and r.RE is not None:
                d_effect += (r.RE / 100.0)
        effective_TR = max(0, math.floor(tr_base * (1 + d_effect)))
        # Effetto A: modifica di RU per il calcolo degli edifici alimentati
        a_effect = 0.0
        for r in active_resources:
            if r.RT == 'A' and r.active_phase and r.active and r.RE is not None:
                a_effect += (r.RE / 100.0) if r.RE >= 0 else - (abs(r.RE) / 100.0)

        # STEP 4: Calcolo degli edifici alimentati
        powered = 0
        for r in active_resources:
            if r.active and r.active_phase:
                effective_RU = max(0, math.floor(r.RU * (1 + a_effect)))
                powered += effective_RU

        # STEP 5: Uso dell'Accumulator (tipo E) per coprire eventuali deficit
        if powered < effective_tm:
            deficit = effective_tm - powered
            for r in active_resources:
                if r.RT == 'E' and r.active and r.active_phase:
                    if deficit <= 0:
                        break
                    available = r.accumulated
                    withdraw = min(deficit, available)
                    r.accumulated -= withdraw
                    deficit -= withdraw
            if deficit > 0:
                powered = 0
        served = min(powered, effective_tx)
        profit = effective_TR * served if powered >= effective_tm else 0
        budget += profit

        # STEP 6: Gestione dell'Accumulator in caso di surplus
        if powered > effective_tx:
            surplus = powered - effective_tx
            accumulators = [r for r in active_resources if r.RT == 'E' and r.active and r.active_phase]
            if accumulators:
                add_each = surplus // len(accumulators)
                for r in accumulators:
                    r.accumulated += add_each

        # STEP 7: Avanza lo stato di ciascuna risorsa e rimuove quelle non attive
        new_active = []
        for r in active_resources:
            r.advance_turn()
            if r.active:
                new_active.append(r)
        active_resources = new_active

    print("\n".join(output))

if __name__ == "__main__":
    main()
