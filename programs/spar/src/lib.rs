use anchor_lang::prelude::*;

declare_id!("6sparPULSE111111111111111111111111111111111"); // Placeholder ID

#[program]
pub mod sovereign_pulse_agent_registry {
    use super::*;

    pub fn register_agent(ctx: Context<RegisterAgent>, name: String, agent_id: String) -> Result<()> {
        let agent = &mut ctx.accounts.agent_record;
        agent.owner = *ctx.accounts.owner.key;
        agent.name = name;
        agent.agent_id = agent_id;
        agent.ptsi_score = 0;
        agent.last_verification_hash = [0u8; 32];
        
        msg!("Agent {} registered successfully!", agent.name);
        Ok(())
    }

    pub fn update_isnād_proof(ctx: Context<UpdateProof>, ptsi_score: u32, verification_hash: [u8; 32]) -> Result<()> {
        let agent = &mut ctx.accounts.agent_record;
        
        // Only the owner can update the proof for this agent
        require_keys_eq!(agent.owner, *ctx.accounts.owner.key, SPAR_ErrorCode::UnauthorizedUpdate);
        
        agent.ptsi_score = ptsi_score;
        agent.last_verification_hash = verification_hash;
        agent.last_updated = Clock::get()?.unix_timestamp;

        msg!("isnād proof updated for agent {}. New PTSI: {}%", agent.name, ptsi_score as f32 / 100.0);
        Ok(())
    }
}

#[derive(Accounts)]
#[instruction(name: String, agent_id: String)]
pub struct RegisterAgent<'info> {
    #[account(
        init, 
        payer = owner, 
        space = 8 + 32 + 64 + 64 + 4 + 32 + 8,
        seeds = [b"agent", owner.key().as_ref(), agent_id.as_bytes()],
        bump
    )]
    pub agent_record: Account<'info, AgentRecord>,
    #[account(mut)]
    pub owner: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct UpdateProof<'info> {
    #[account(mut)]
    pub agent_record: Account<'info, AgentRecord>,
    pub owner: Signer<'info>,
}

#[account]
pub struct AgentRecord {
    pub owner: Pubkey,
    pub name: String,
    pub agent_id: String,
    pub ptsi_score: u32, // Represented as basis points (1414 = 14.14%)
    pub last_verification_hash: [u8; 32],
    pub last_updated: i64,
}

#[error_code]
pub enum SPAR_ErrorCode {
    #[msg("You are not authorized to update this agent's proof.")]
    UnauthorizedUpdate,
}
