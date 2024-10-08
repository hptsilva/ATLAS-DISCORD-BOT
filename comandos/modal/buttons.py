import discord
import comandos.modal.reacoes as reacoes
from comandos.modal.modal_enquete_editar import Modal_Enquete_Editar

class Menu_Enquete(discord.ui.View):

    def __init__(self):
        super().__init__()
        self.timeout = None

    @discord.ui.button(label='', style=discord.ButtonStyle.green, emoji='✅')
    async def confirmacao1(self, interaction: discord.Interaction, button: discord.ui.Button):

        Reacoes_Enquete = reacoes.Reacoes_Enquete()
        message = interaction.message
        user = interaction.user
        embed = await Reacoes_Enquete.reacoes(message, user, 1)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label='', style=discord.ButtonStyle.red, emoji='⛔')
    async def confirmacao2(self, interaction: discord.Interaction, button: discord.ui.Button):

        Reacoes_Enquete = reacoes.Reacoes_Enquete()
        message = interaction.message
        user = interaction.user
        embed = await Reacoes_Enquete.reacoes(message, user, 2)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label='', style=discord.ButtonStyle.blurple, emoji='❔')
    async def confirmacao3(self, interaction: discord.Interaction, button: discord.ui.Button):

        Reacoes_Enquete = reacoes.Reacoes_Enquete()
        message = interaction.message
        user = interaction.user
        embed = await Reacoes_Enquete.reacoes(message, user, 3)
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label='EDITAR', style=discord.ButtonStyle.gray)
    async def editar(self, interaction: discord.Interaction, button: discord.ui.Button):

        message = interaction.message
        author = message.interaction_metadata.user
        if interaction.user == author:
            pass
        else:
            await interaction.response.send_message('Apenas o criador do evento pode editá-lo.', ephemeral=True)
            return
        await interaction.response.send_modal(Modal_Enquete_Editar())

    @discord.ui.button(label='CANCELAR', style=discord.ButtonStyle.gray)
    async def cancelar(self, interaction: discord.Interaction, button: discord.ui.Button):

        message = interaction.message
        author = message.interaction_metadata.user
        if interaction.user == author:
            Reacoes_Enquete = reacoes.Reacoes_Enquete()
            message = interaction.message
            embed = await Reacoes_Enquete.reacoes(message, author, 4)
            await interaction.response.edit_message(embed=embed, view=None)
            self.stop()
        else:
            await interaction.response.send_message('Apenas o criador do evento pode cancelá-lo.', ephemeral=True)

    @discord.ui.button(label='CONCLUIR', style=discord.ButtonStyle.gray)
    async def concluir(self, interaction: discord.Interaction, button: discord.ui.Button):
        message = interaction.message
        author = message.interaction_metadata.user
        if interaction.user == author:
            Reacoes_Enquete = reacoes.Reacoes_Enquete()
            message = interaction.message
            embed = await Reacoes_Enquete.reacoes(message, author, 5)
            await interaction.response.edit_message(embed=embed, view=None)
            self.stop()
        else:
            await interaction.response.send_message('Apenas o criador do evento pode concluí-lo.', ephemeral=True)
