"
c = Candidate(...user)
c = Candidate.updateStep(respostasPreviousStep)
updated = candidadeRepository.updateStep(adaptCandidateToRepository(c))
newC = Candidate(updated)
"

(let [c (logic/->candidate user)
      c (logic/update-candidate-based-on-stuff respostas-previous-step)]
  (protocols/update db c)
  c)
