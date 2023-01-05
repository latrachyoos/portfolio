<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class Form1
    Inherits System.Windows.Forms.Form

    'Form overrides dispose to clean up the component list.
    <System.Diagnostics.DebuggerNonUserCode()> _
    Protected Overrides Sub Dispose(ByVal disposing As Boolean)
        Try
            If disposing AndAlso components IsNot Nothing Then
                components.Dispose()
            End If
        Finally
            MyBase.Dispose(disposing)
        End Try
    End Sub

    'Required by the Windows Form Designer
    Private components As System.ComponentModel.IContainer

    'NOTE: The following procedure is required by the Windows Form Designer
    'It can be modified using the Windows Form Designer.  
    'Do not modify it using the code editor.
    <System.Diagnostics.DebuggerStepThrough()> _
    Private Sub InitializeComponent()
        Me.cmbcat = New System.Windows.Forms.ComboBox()
        Me.dgv = New System.Windows.Forms.DataGridView()
        Me.IDProdotto = New System.Windows.Forms.DataGridViewTextBoxColumn()
        Me.nomeProdotto = New System.Windows.Forms.DataGridViewTextBoxColumn()
        Me.PrezzoUnitario = New System.Windows.Forms.DataGridViewTextBoxColumn()
        Me.Scorte = New System.Windows.Forms.DataGridViewTextBoxColumn()
        Me.livelloDiRiordino = New System.Windows.Forms.DataGridViewTextBoxColumn()
        Me.lvlriordino = New System.Windows.Forms.CheckBox()
        Me.txtnomeprodotto = New System.Windows.Forms.TextBox()
        Me.txtpu = New System.Windows.Forms.TextBox()
        Me.txtscorte = New System.Windows.Forms.TextBox()
        Me.txtldo = New System.Windows.Forms.TextBox()
        Me.cmbadd = New System.Windows.Forms.ComboBox()
        Me.Button1 = New System.Windows.Forms.Button()
        CType(Me.dgv, System.ComponentModel.ISupportInitialize).BeginInit()
        Me.SuspendLayout()
        '
        'cmbcat
        '
        Me.cmbcat.FormattingEnabled = True
        Me.cmbcat.Location = New System.Drawing.Point(12, 12)
        Me.cmbcat.Name = "cmbcat"
        Me.cmbcat.Size = New System.Drawing.Size(158, 21)
        Me.cmbcat.TabIndex = 0
        Me.cmbcat.Text = "Seleziona una categoria"
        '
        'dgv
        '
        Me.dgv.AllowUserToAddRows = False
        Me.dgv.AllowUserToDeleteRows = False
        Me.dgv.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize
        Me.dgv.Columns.AddRange(New System.Windows.Forms.DataGridViewColumn() {Me.IDProdotto, Me.nomeProdotto, Me.PrezzoUnitario, Me.Scorte, Me.livelloDiRiordino})
        Me.dgv.Location = New System.Drawing.Point(176, 12)
        Me.dgv.Name = "dgv"
        Me.dgv.ReadOnly = True
        Me.dgv.Size = New System.Drawing.Size(571, 271)
        Me.dgv.TabIndex = 1
        '
        'IDProdotto
        '
        Me.IDProdotto.Frozen = True
        Me.IDProdotto.HeaderText = "ID Prodotto"
        Me.IDProdotto.Name = "IDProdotto"
        Me.IDProdotto.ReadOnly = True
        '
        'nomeProdotto
        '
        Me.nomeProdotto.HeaderText = "Nome Prodotto"
        Me.nomeProdotto.Name = "nomeProdotto"
        Me.nomeProdotto.ReadOnly = True
        '
        'PrezzoUnitario
        '
        Me.PrezzoUnitario.HeaderText = "Prezzo Unitario"
        Me.PrezzoUnitario.Name = "PrezzoUnitario"
        Me.PrezzoUnitario.ReadOnly = True
        '
        'Scorte
        '
        Me.Scorte.HeaderText = "Scorte"
        Me.Scorte.Name = "Scorte"
        Me.Scorte.ReadOnly = True
        '
        'livelloDiRiordino
        '
        Me.livelloDiRiordino.HeaderText = "Livello Di Riordino"
        Me.livelloDiRiordino.Name = "livelloDiRiordino"
        Me.livelloDiRiordino.ReadOnly = True
        '
        'lvlriordino
        '
        Me.lvlriordino.AutoSize = True
        Me.lvlriordino.Location = New System.Drawing.Point(12, 39)
        Me.lvlriordino.Name = "lvlriordino"
        Me.lvlriordino.Size = New System.Drawing.Size(158, 30)
        Me.lvlriordino.TabIndex = 2
        Me.lvlriordino.Text = "Mostra prodotti con livello " & Global.Microsoft.VisualBasic.ChrW(13) & Global.Microsoft.VisualBasic.ChrW(10) & "di riordino inferiori alle scorte"
        Me.lvlriordino.UseVisualStyleBackColor = True
        '
        'txtnomeprodotto
        '
        Me.txtnomeprodotto.Location = New System.Drawing.Point(11, 115)
        Me.txtnomeprodotto.Name = "txtnomeprodotto"
        Me.txtnomeprodotto.Size = New System.Drawing.Size(159, 20)
        Me.txtnomeprodotto.TabIndex = 3
        Me.txtnomeprodotto.Text = "Nome Prodotto"
        '
        'txtpu
        '
        Me.txtpu.Location = New System.Drawing.Point(11, 141)
        Me.txtpu.Name = "txtpu"
        Me.txtpu.Size = New System.Drawing.Size(159, 20)
        Me.txtpu.TabIndex = 4
        Me.txtpu.Text = "Prezzo Unitario"
        '
        'txtscorte
        '
        Me.txtscorte.Location = New System.Drawing.Point(11, 167)
        Me.txtscorte.Name = "txtscorte"
        Me.txtscorte.Size = New System.Drawing.Size(159, 20)
        Me.txtscorte.TabIndex = 5
        Me.txtscorte.Text = "Scorte"
        '
        'txtldo
        '
        Me.txtldo.Location = New System.Drawing.Point(11, 193)
        Me.txtldo.Name = "txtldo"
        Me.txtldo.Size = New System.Drawing.Size(159, 20)
        Me.txtldo.TabIndex = 6
        Me.txtldo.Text = "Livello di Riordino"
        '
        'cmbadd
        '
        Me.cmbadd.FormattingEnabled = True
        Me.cmbadd.Location = New System.Drawing.Point(11, 219)
        Me.cmbadd.Name = "cmbadd"
        Me.cmbadd.Size = New System.Drawing.Size(159, 21)
        Me.cmbadd.TabIndex = 7
        Me.cmbadd.Text = "Seleziona una categoria"
        '
        'Button1
        '
        Me.Button1.BackColor = System.Drawing.Color.Transparent
        Me.Button1.Location = New System.Drawing.Point(11, 246)
        Me.Button1.Name = "Button1"
        Me.Button1.Size = New System.Drawing.Size(159, 37)
        Me.Button1.TabIndex = 8
        Me.Button1.Text = "AGGIUNGI"
        Me.Button1.UseVisualStyleBackColor = False
        '
        'Form1
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(766, 298)
        Me.Controls.Add(Me.Button1)
        Me.Controls.Add(Me.cmbadd)
        Me.Controls.Add(Me.txtldo)
        Me.Controls.Add(Me.txtscorte)
        Me.Controls.Add(Me.txtpu)
        Me.Controls.Add(Me.txtnomeprodotto)
        Me.Controls.Add(Me.lvlriordino)
        Me.Controls.Add(Me.dgv)
        Me.Controls.Add(Me.cmbcat)
        Me.Name = "Form1"
        Me.Text = "Form1"
        CType(Me.dgv, System.ComponentModel.ISupportInitialize).EndInit()
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub
    Friend WithEvents cmbcat As System.Windows.Forms.ComboBox
    Friend WithEvents dgv As System.Windows.Forms.DataGridView
    Friend WithEvents IDProdotto As System.Windows.Forms.DataGridViewTextBoxColumn
    Friend WithEvents nomeProdotto As System.Windows.Forms.DataGridViewTextBoxColumn
    Friend WithEvents PrezzoUnitario As System.Windows.Forms.DataGridViewTextBoxColumn
    Friend WithEvents Scorte As System.Windows.Forms.DataGridViewTextBoxColumn
    Friend WithEvents livelloDiRiordino As System.Windows.Forms.DataGridViewTextBoxColumn
    Friend WithEvents lvlriordino As System.Windows.Forms.CheckBox
    Friend WithEvents txtnomeprodotto As System.Windows.Forms.TextBox
    Friend WithEvents txtpu As System.Windows.Forms.TextBox
    Friend WithEvents txtscorte As System.Windows.Forms.TextBox
    Friend WithEvents txtldo As System.Windows.Forms.TextBox
    Friend WithEvents cmbadd As System.Windows.Forms.ComboBox
    Friend WithEvents Button1 As System.Windows.Forms.Button

End Class
