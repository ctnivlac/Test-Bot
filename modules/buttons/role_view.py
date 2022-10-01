import nextcord
from config import *

VIEW_NAME = "RoleView"

def custom_id(view: str, id: int) -> str:
    return f"{BOT_NAME}:{view}:{id}"

class RoleView(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    async def handle_click(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        role = interaction.guild.get_role(int(button.custom_id.split(":")[-1]))

        assert isinstance(role, nextcord.Role)

        if role in interaction.user.roles:
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(
                f"Your {button.label} role has been removed", ephemeral=True
            )
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(
                f"You have been given the {button.label} role", ephemeral=True
            )
            
    @nextcord.ui.button(
        label="Engineering", 
        emoji= ENGINEER_EMOJI,
        style=nextcord.ButtonStyle.primary,
        custom_id=custom_id(VIEW_NAME, ENGINEER_ROLE_ID)
    )
    async def engineering_button(self, button, interaction):
        await self.handle_click(button, interaction)

    @nextcord.ui.button(
        label="Operations", 
        emoji=OPERATIONS_EMOJI,
        style=nextcord.ButtonStyle.primary,
        custom_id=custom_id(VIEW_NAME, OPERATIONS_ROLE_ID)
    )
    async def operations_button(self, button, interaction):
        await self.handle_click(button, interaction)