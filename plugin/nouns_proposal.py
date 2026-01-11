# -*- coding: utf-8 -*-

import json
import urllib.request
import webbrowser
from flox import Flox


class NounsProposal(Flox):
    
    NOUNCIL_URL = "https://nouncil.club/proposal/"
    PROPOSALS_URL = "https://raw.githubusercontent.com/XppaiCyberr/nounsProposals/refs/heads/main/proposals.json"
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.proposals = self._load_proposals()
    
    def _load_proposals(self):
        """Fetch proposals from remote URL"""
        try:
            with urllib.request.urlopen(self.PROPOSALS_URL, timeout=10) as response:
                data = json.loads(response.read().decode('utf-8'))
                return data.get('data', {}).get('proposals', [])
        except Exception as e:
            self.logger.error(f"Error fetching proposals: {e}")
            return []
    
    def query(self, query):
        """Search proposals based on user query"""
        q = query.strip().lower()
        
        if not q:
            # Show all proposals (limited to first 20 for performance)
            for proposal in self.proposals[:20]:
                self._add_proposal_item(proposal)
            
            if len(self.proposals) > 20:
                self.add_item(
                    title=f"... and {len(self.proposals) - 20} more proposals",
                    subtitle="Type to search for specific proposals",
                    icon=self.icon
                )
        else:
            # Search by ID or title
            matches = []
            for proposal in self.proposals:
                prop_id = proposal.get('id', '')
                title = proposal.get('title', '').lower()
                proposer = proposal.get('proposer', {})
                ens = proposer.get('ens', '') or ''
                
                # Match by ID, title, or proposer ENS
                if (q == prop_id or 
                    q in title or 
                    q in ens.lower()):
                    matches.append(proposal)
            
            if matches:
                for proposal in matches[:20]:
                    self._add_proposal_item(proposal)
                
                if len(matches) > 20:
                    self.add_item(
                        title=f"... and {len(matches) - 20} more matches",
                        subtitle="Be more specific to narrow results",
                        icon=self.icon
                    )
            else:
                self.add_item(
                    title="No proposals found",
                    subtitle=f"No matches for '{query}'",
                    icon=self.icon
                )
    
    def _add_proposal_item(self, proposal):
        """Add a proposal item to the results"""
        prop_id = proposal.get('id', '')
        title = proposal.get('title', 'Untitled')
        status = proposal.get('status', 'Unknown')
        proposer = proposal.get('proposer', {})
        ens = proposer.get('ens')
        address = proposer.get('id', '')
        
        # Format proposer info
        if ens:
            proposer_info = ens
        else:
            proposer_info = f"{address[:6]}...{address[-4:]}" if address else "Unknown"
        
        self.add_item(
            title=f"#{prop_id}: {title}",
            subtitle=f"[{status}] by {proposer_info}",
            icon=self.icon,
            method=self.open_proposal,
            parameters=[prop_id],
            context=[prop_id, title]
        )
    
    def open_proposal(self, prop_id):
        """Open the proposal URL in the browser"""
        url = f"{self.NOUNCIL_URL}{prop_id}"
        webbrowser.open(url)
    
    def context_menu(self, data):
        """Show context menu for a proposal"""
        if data:
            prop_id = data[0]
            title = data[1] if len(data) > 1 else ''
            
            self.add_item(
                title=f"Open Proposal #{prop_id}",
                subtitle=f"Open in browser: {self.NOUNCIL_URL}{prop_id}",
                icon=self.icon,
                method=self.open_proposal,
                parameters=[prop_id]
            )


if __name__ == "__main__":
    NounsProposal()
