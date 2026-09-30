"""Rule-based architecture risk detection from analysis results."""
from __future__ import annotations

def validate(arguments):
    if not isinstance(arguments, dict): raise TypeError("arguments must be an object")
    analysis=arguments.get('analysis')
    if not isinstance(analysis, dict): raise ValueError('analysis is required')

def execute(arguments):
    validate(arguments); a=arguments['analysis']; risks=[]
    langs=a.get('language_counts',{})
    if a.get('file_count',0)==0: risks.append({'id':'empty-repository','severity':'high','finding':'No analyzable source files were found.','evidence':'file_count=0'})
    if len(langs)>=5: risks.append({'id':'polyglot-complexity','severity':'medium','finding':'Multiple implementation languages increase build and operational coordination cost.','evidence':sorted(langs)})
    if a.get('file_count',0)>1000: risks.append({'id':'large-repository-surface','severity':'medium','finding':'Large source surface may increase change coupling and analysis cost.','evidence':a['file_count']})
    return {'risk_count':len(risks),'risks':risks,'method':'deterministic heuristics; findings require repository-specific review'}
